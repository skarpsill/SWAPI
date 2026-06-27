---
title: "Insert and Modify Datum Target Symbol Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Modify_Datum_Target_Symbol_Example_VB.htm"
---

# Insert and Modify Datum Target Symbol Example (VBA)

This example shows how to insert and modify a datum target symbol.

```vb
'------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified part document exists.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the specified part document.
 ' 2. Inserts a datum target symbol on the selected
 '    face.
 ' 3. Gets and modifies the datum target symbol's reference label.
 ' 4. Examine the Immediate window and graphics area.
 '
 ' NOTE: Because the part document is used elsewhere,
 ' do not save any changes.
 '------------------------------------------------------------
 Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swDatumTargetSym As SldWorks.DatumTargetSym
 Dim fileName As String
 Dim status As Boolean
 Dim errors As Long
 Dim warnings As Long

 Sub main()
     Set swApp = Application.SldWorks
     'Open part document
     fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\holecube.sldprt"
     Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

     'Select face for datum target symbol
     Set swModelDocExt = swModel.Extension
     status = swModelDocExt.SelectByID2("", "FACE", -7.23565448987529E-03, -2.59480787517532E-02, 0, False, 0, Nothing, 0)

     'Insert datum target symbol
     Set swDatumTargetSym = swModelDocExt.InsertDatumTargetSymbol3("a", "", "", 0, False, 0.003, 0.03, "3", "", True, 12, 0, True, False, True, swMoveableDatumStyle_Horizontal)

     'Get and set datum reference label
     Debug.Print ("Current reference label: " & swDatumTargetSym.GetDatumReferenceLabel(0))
     status = swDatumTargetSym.SetDatumReferenceLabel(0, "b")
     Debug.Print ("Modified reference label: " & swDatumTargetSym.GetDatumReferenceLabel(0))
End Sub
```
