from ViewData import Ui_Form
from genericGado import scriptGado
import toAdd_Edit_IG
import QT_tblViewUtility
import QT_msg
import toAdd_Edit_IM
import toAdd_Edit_IN
import toAdd_Edit_IR
from PyQt5.Qt import QDialog
from toAcontecimentos import toAcontecimentos
from toIntroducaoGeral import toIntroducaoGeral
from toAddNovo import toAddNovo
from toAddMortos import toAddMortos
from toAddRetiradas import toAddRetirados
from toViewCategories import toViewCategories
import sys
from PyQt5.QtWidgets import *
#Set TO Null after a change
#self.clickedVal
#
class toViewData(scriptGado, Ui_Form):
    def __init__(self, parente= None, dbCon=None):
        super(toViewData, self).__init__(parente)
        self.setupUi(self)
        
        self.setDicts()
#         self.setCombBox()
        self.setTheView()
        self.clickedVal=None
        self.TV.clicked.connect(self.clickedField)
        #self.setClicked()
        self.PBAddIR.clicked.connect(self._teste_)
        self.PBAddIG.clicked.connect(self._teste_)
        self.PBAddIM.clicked.connect(self._teste_)
        self.PBAddIN.clicked.connect(self._teste_)
        self.PBEditIG.clicked.connect(self._teste_)
        
    def openToInsert(self):
        objName = self.sender().objectName()
        view = self.dictInserts.get(objName)()
        view.exec_()

    def openToEdit(self):
        if self.clickedVal is not None:
            objName = self.sender().objectName()
            view = self.dictEdits.get(objName)(lstToEdit = self.clickedVal)
            view.exec_()
        else:
            QT_msg.aviso(txt= "Porfavor <b>Selecione um elemento na tabela</b>  para Editar")
    
    def setClicked(self):
        lstInsert = [self.PBAddIG, self.PBAddIM, self.PBAddIN, self.PBAddIR]
        lstToEdit = [self.PBEditIG, self.PBEditIM, self.PBEditIN, self.PBEditIR]
        
        for add in lstInsert:
            add.clicked.connect(self.openToInsert)
            
        for edit in lstToEdit:
            edit.clicked.connect(self.openToEdit)
    

    def _teste_(self):
        sender = self.sender().objectName()
        
        if sender == 'PBAddIR':
            frmAcontecimento = toAcontecimentos()
            frmAcontecimento.exec_()
        
        elif sender == 'PBAddIG':
            frmGeral = toIntroducaoGeral()
            frmGeral.exec_()
            
        elif sender == 'PBAddIN':
            frmNovos = toAddNovo()
            frmNovos.exec_()
        
        elif sender == 'PBAddIM':
            frmMortos = toAddMortos()
            frmMortos.exec_()
            
        elif sender == 'PBEditIG':
            frmGeral = toViewCategories()#Name is not related, i know, i'll change
            frmGeral.exec_()

    def setDicts(self):
        self.dictFields={
                'quer': '''SELECT tbl1.id as "Cod.", tbl2.nome as "Categoria", sexo as "Sexo", 
                            data_nascimento as "Data de Nascimento", total as "Total Existente", data_edicao as "Ultima Edicao"
                              FROM public.tbl_gado as tbl1
                              inner join tbl_categorias as tbl2 
                              on tbl1.id_categoria = tbl2.id''',
                        
                'fldToHide':[True, False, False, False, False, False],
                
                'sizeCol':[0, 170, 140, 200, 150, 150]
                        }
        
        
        self.dictCB = {
                       'quer': ["select null as id, '-Categoria-' as nome union all select id, nome from tbl_categorias",
                                ''' select null as id, '-Sexo-' as nome union all 
                                    select 'M' as id, 'Macho' as nome union all 
                                    select 'F' as id, 'Femea' as nome'''
                                ],
                       'widgets': [self.CBCagegoria, self.CBSexo] 
                        }
        
        self.dictInserts = {'PBAddIG': toAdd_Edit_IG.toIntroducaoGeral,
                            'PBAddIM': toAdd_Edit_IM.toIntroducaoMortos,
                            'PBAddIN': toAdd_Edit_IN.toIntroducaoNascidos,
                            'PBAddIR': toAdd_Edit_IR.toIntroducaoRemovidos
                            }
        
        
        self.dictEdits = { 'PBEditIG': toAdd_Edit_IG.toIntroducaoGeral,
                        'PBEditIM': toAdd_Edit_IM.toIntroducaoMortos,
                        'PBEditIN': toAdd_Edit_IN.toIntroducaoNascidos,
                        'PBEditIR': toAdd_Edit_IR.toIntroducaoRemovidos,
                        }
         
        
if __name__ == "__main__":     
    app = QApplication(sys.argv)
    formMain = toViewData()
    app.setStyle(QStyleFactory.create("Fusion"))
    formMain.exec_()    