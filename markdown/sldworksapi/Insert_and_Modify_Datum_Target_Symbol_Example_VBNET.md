---
title: "Insert and Modify Datum Target Symbol Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Modify_Datum_Target_Symbol_Example_VBNET.htm"
---

# Insert and Modify Datum Target Symbol Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public Sub main()

         Dim swModel As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim swDatumTargetSym As DatumTargetSym
         Dim fileName As String
         Dim status As Boolean
         Dim errors As Integer
         Dim warnings As Integer

         'Open part document
         fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\holecube.sldprt"
         swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

         'Select face for datum target symbol
         swModelDocExt = swModel.Extension
         status = swModelDocExt.SelectByID2("", "FACE", -0.00723565448987529, -0.0259480787517532, 0, False, 0, Nothing, 0)

         'Insert datum target symbol
         swDatumTargetSym = swModelDocExt.InsertDatumTargetSymbol3("a", "", "", 0, False, 0.003, 0.03, "3", "", True, 12, 0, True, False, True,  swMoveableDatumStyle_e.swMoveableDatumStyle_Horizontal)

         'Get and set datum reference label
         Debug.Print("Current reference label: " & swDatumTargetSym.GetDatumReferenceLabel(0))
         status = swDatumTargetSym.SetDatumReferenceLabel(0, "b")
         Debug.Print("Modified reference label: " & swDatumTargetSym.GetDatumReferenceLabel(0))

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
