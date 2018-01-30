'''
Created on 05/01/2018

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import QDialog
import GenericIntroducoes
from introducaoGeral import Ui_Form

class toIntroducaoGeral(GenericIntroducoes.GenericIntroducao, Ui_Form):
    def __init__(self, parente=None, lstToEdit=None):
        super(toIntroducaoGeral, self).__init__(parente)
        self.setupUi(self)
        
        self.setDict()
        self.setCombBox()
        self.lstToEdit = lstToEdit
        self.toFill()
        
    def setDict(self):
        self.dictFields={
                            'lstName': ["id", "id_categoria", "sexo", "data_nascimento", 
                                        "total_mortos", "total_vivos", "total"],
                             
                            'lstToQuote': [False, True, True, True,
                                            False, False, False],
                            
                            'lstWidget': [self.LECod, self.CBCategoria, self.CBSexo, self.DTEData, 
                                          self.SBTotalMortos, self.SBTotalVivos, self.SBTotal],
                             
                            'lstRel': [False, True, False, False,
                                        False, False, False],
                            
                            'lstDefault':[False, False, False, False,
                                           False, False, False],
                            
                            'lstUpercase':[False, False, False, False, 
                                           False, False, False]
                        }
        
        self.dictCB = {
                       'quer': ["select null as id, '-Categoria-' as nome union all select id, nome from tbl_categorias",
                                ''' select null as id, '-Sexo-' as nome union all 
                                    select 'M' as id, 'Macho' as nome union all 
                                    select 'F' as id, 'Femea' as nome'''],
                       'widgets': [self.CBCategoria, self.CBSexo] 
                        }
