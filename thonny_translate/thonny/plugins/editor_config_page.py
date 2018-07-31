import tkinter as tk
from tkinter import ttk

from thonny.config_ui import ConfigurationPage
from thonny.globals import get_workbench
import logging


class EditorConfigurationPage(ConfigurationPage):
    
    def __init__(self, master):
        ConfigurationPage.__init__(self, master)
        
        try:
            self.add_checkbox("view.name_highlighting", "高亮匹配名称")
        except:
            # name matcher may have been disabled
            logging.warning("Couldn't create name matcher checkbox")
            
        try:
            self.add_checkbox("view.locals_highlighting", "高亮本地变量")
        except:
            # locals highlighter may have been disabled
            logging.warning("Couldn't create name locals highlighter checkbox")
            
        self.add_checkbox("view.paren_highlighting", "高亮括号")
        self.add_checkbox("view.syntax_coloring", "高亮关键字")
        
        self.add_checkbox("edit.tab_complete_in_editor", "在编辑器内允许Tab自动补全", 
                          columnspan=2, pady=(20,0), )
        self.add_checkbox("edit.tab_complete_in_shell",  "在命令行内允许Tab自动补全",
                          columnspan=2)
        
        self.add_checkbox("view.show_line_numbers", "显示行号", pady=(20,0))
        self._line_length_var = get_workbench().get_variable("view.recommended_line_length")
        label = ttk.Label(self, text="推荐最大行宽\n(设置为0时不显示边线)")
        label.grid(row=7, column=0, sticky=tk.W)
        self._line_length_combo = ttk.Combobox(self, width=4,
                                        exportselection=False,
                                        textvariable=self._line_length_var,
                                        state='readonly',
                                        values=[0,60,70,80,90,100,110,120])
        self._line_length_combo.grid(row=7, column=1, sticky=tk.E)
        
        self.columnconfigure(0, weight=1)
    
    def apply(self):
        ConfigurationPage.apply(self)
        get_workbench().get_editor_notebook().update_appearance()
    

def load_plugin():
    get_workbench().add_configuration_page("编辑器", EditorConfigurationPage)
