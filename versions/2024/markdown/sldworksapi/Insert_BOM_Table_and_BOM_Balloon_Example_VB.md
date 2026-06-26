---
title: "Insert BOM Table and BOM Balloon Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_BOM_Table_and_BOM_Balloon_Example_VB.htm"
---

# Insert BOM Table and BOM Balloon Example (VBA)

## Insert BOM Table and BOM Balloon (VBA)

This example shows how to insert a BOM table and a BOM balloon in a
drawing document.

```
'------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Inserts a parts-only BOM table.
' 2. Inserts a split-circle BOM balloon, which uses the BOM
'    table item number for its upper text,
'    to the selected edge.
' 3. Zoom to area and examine both the BOM table and BOM
'    balloon to verify.
'
' NOTE: Because this drawing document is used elsewhere,
' do not save any changes.
'-------------------------------------------------
```

```vb
Option Explicit

Sub main()

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swApp kadov_tag{{<spaces>}}                  kadov_tag{{</spaces>}}As SldWorks.SldWorks
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swModel kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}As SldWorks.ModelDoc2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swModelDocExt kadov_tag{{<spaces>}}          kadov_tag{{</spaces>}}As SldWorks.ModelDocExtension
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swDrawing kadov_tag{{<spaces>}}              kadov_tag{{</spaces>}}As SldWorks.DrawingDoc
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swView kadov_tag{{<spaces>}}                 kadov_tag{{</spaces>}}As SldWorks.View
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swBOMAnnotation kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}As SldWorks.BomTableAnnotation
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swBOMFeature kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}As SldWorks.BomFeature
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swNote kadov_tag{{<spaces>}}                 kadov_tag{{</spaces>}}As SldWorks.Note
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim boolstatus kadov_tag{{<spaces>}}             kadov_tag{{</spaces>}}As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim AnchorType kadov_tag{{<spaces>}}             kadov_tag{{</spaces>}}As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim BomType kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim Configuration kadov_tag{{<spaces>}}          kadov_tag{{</spaces>}}As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim TableTemplate kadov_tag{{<spaces>}}          kadov_tag{{</spaces>}}As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swApp = Application.SldWorks
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swDrawing = swModel
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swModelDocExt = swModel.Extension
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swDrawing.ActivateView("Drawing View1")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swView = swDrawing.ActiveDrawingView
kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Insert parts-only BOM table
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}AnchorType = swBOMConfigurationAnchor_TopLeft
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}BomType = swBomType_PartsOnly
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Configuration = ""
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}TableTemplate = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\bom-standard.sldbomtbt"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swBOMAnnotation = swView.InsertBomTable2(False, 0.4, 0.3, AnchorType, BomType, Configuration, TableTemplate)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swBOMFeature = swBOMAnnotation.BomFeature

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Print the name of the configuration used for the BOM table
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Name of configuration used for BOM table: " & swBOMFeature.Configuration
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Insert BOM balloon for the selected edge
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.1205506330468, 0.261655309417, -4.000000000133E-04, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swNote = swModelDocExt.InsertBOMBalloon(swBS_SplitCirc, swBF_Tightest, swBalloonTextItemNumber, "", swBalloonTextCustom, "Lower text", swBF_UserDef, True, 2, "Denotation Text")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get whether balloon is a BOM balloon;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' if so, print the name of the BOM balloon
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If swNote.IsBomBalloon Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print ("Name of BOM balloon: " & swNote.GetName)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
```
