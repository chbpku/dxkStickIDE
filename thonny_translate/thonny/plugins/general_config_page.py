import tkinter as tk
from tkinter import ttk

from thonny.config_ui import ConfigurationPage
from thonny.globals import get_workbench


class GeneralConfigurationPage(ConfigurationPage):
    
    def __init__(self, master):
        ConfigurationPage.__init__(self, master)
        
        self._single_instance_var = get_workbench().get_variable("general.single_instance")
        self._single_instance_checkbox = ttk.Checkbutton(self,
                                                         text="只允许单个Thonny窗口运行", 
                                                      variable=self._single_instance_var)
        self._single_instance_checkbox.grid(row=1, column=0, sticky=tk.W)
        
        self._expert_var = get_workbench().get_variable("general.expert_mode")
        self._expert_checkbox = ttk.Checkbutton(self, text="专业模式", variable=self._expert_var)
        self._expert_checkbox.grid(row=2, column=0, sticky=tk.W)
        
        self._debug_var = get_workbench().get_variable("general.debug_mode")
        self._debug_checkbox = ttk.Checkbutton(self, text="调试模式", variable=self._debug_var)
        self._debug_checkbox.grid(row=3, column=0, sticky=tk.W)
        
        reopen_label = ttk.Label(self, text="注意！该页内容更改后需重启Thonny生效")
        reopen_label.grid(row=4, column=0, sticky=tk.W, pady=20)
        
        
        self.columnconfigure(0, weight=1)

            
    

def load_plugin():
    get_workbench().add_configuration_page("通用", GeneralConfigurationPage)
