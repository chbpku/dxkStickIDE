from .translation import translate

# load translating wrappers first
load_order_key = "\0"


def trans_wrap(hook_obj, func_name, arg_ind, arg_name):
    func = getattr(hook_obj, func_name)

    def dummy(self, *a, **kw):
        if len(a) > arg_ind:
            a = list(a)
            a[arg_ind] = translate(a[arg_ind])
        elif arg_name in kw:
            kw[arg_name] = translate(kw[arg_name])
        return func(self, *a, **kw)

    setattr(hook_obj, func_name, dummy)


def load_plugin():
    '''注入翻译代码'''
    from thonny import get_workbench
    from thonny.workbench import BackendSpec, Workbench as wb
    from thonny.config_ui import ConfigurationPage as cp
    from tkinter.ttk import Label
    bench = get_workbench()

    # all commands
    trans_wrap(wb, '_publish_command', 2, 'command_label')

    # all view titles
    for view in bench._view_records.values():  # before
        view['label'] = translate(view['label'])
    trans_wrap(wb, 'add_view', 1, 'label')  # after

    # all menus
    trans_wrap(wb, 'get_menu', 1, 'label')

    # config page titles
    trans_wrap(wb, 'add_configuration_page', 0, 'title')

    # config pages
    trans_wrap(cp, 'add_checkbox', 1, 'description')
    trans_wrap(cp, 'add_checkbox', 7, 'tooltip')
    trans_wrap(Label, '__init__', 1000, 'text')

    # interpreter labels
    for k, v in bench._backends.items():  # before
        bench._backends[k] = v._replace(description=translate(v.description))
    trans_wrap(wb, 'add_backend', 2, 'description')  # after
