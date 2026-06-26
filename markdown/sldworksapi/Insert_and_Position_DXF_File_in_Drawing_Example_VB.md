---
title: "Insert and Position DXF/DWG File in Drawing Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Position_DXF_File_in_Drawing_Example_VB.htm"
---

# Insert and Position DXF/DWG File in Drawing Example (VBA)

This example shows how to insert and position a DXF/DWG file in a drawing.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing.
 ' 2. Replace DXF_file_path with the pathname of an existing DXF/DWG file.
 ' 3. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Inserts the DXF/DWG file per the specified import data.
 ' 2. Inspect the Immediate window.
 '---------------------------------------------------------------------------
 Option Explicit
Sub main()
    Const sDwgFileName                  As String = "DXF_file_path"
    Dim swApp As SldWorks.SldWorks
     Dim swModel As SldWorks.ModelDoc2
     Dim swModelView As SldWorks.ModelView
     Dim swDraw As SldWorks.DrawingDoc
     Dim swFeatMgr As SldWorks.FeatureManager
     Dim swFeat As SldWorks.Feature
     Dim swSketch As SldWorks.Sketch
     Dim swView As SldWorks.View
     Dim vPos As Variant
     Dim bRet As Boolean
     Dim importData As SldWorks.ImportDxfDwgData

    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelView = swModel.ActiveView

    bRet = swModel.Extension.SelectByID2("Sheet1", "SHEET", 0#, 0#, 0, False, 0, Nothing, 0)
    Set swDraw = swModel
     Set swFeatMgr = swModel.FeatureManager
     Set importData = swApp.GetImportFileData(sDwgFileName)

    ' Unit
     importData.LengthUnit("") = SwConst.swLengthUnit_e.swINCHES

    ' Position
     bRet = importData.SetPosition("", swDwgEntitiesCentered, 0, 0)

    ' Sheet scale
     bRet = importData.SetSheetScale("", 1#, 2#)

    ' Paper size
     bRet = importData.SetPaperSize("", SwConst.swDwgPaperSizes_e.swDwgPaperAsize, 0#, 0#)

    ' Import method
     importData.ImportMethod("") = swImportDxfDwg_ImportMethod_e.swImportDxfDwg_ImportToExistingDrawing

    ' Import file with importData
     Set swFeat = swFeatMgr.InsertDwgOrDxfFile2(sDwgFileName, importData)

     Set swSketch = swFeat.GetSpecificFeature2
    Set swView = swDraw.GetFirstView

    Do While Not swView Is Nothing
         If swSketch Is swView.GetSketch Then
             Exit Do
         End If
         Set swView = swView.GetNextView
     Loop

    vPos = swView.Position

    Debug.Print "File = " & swModel.GetPathName
     Debug.Print "  Sketch       = " & swFeat.Name
     Debug.Print "  View         = " & swView.Name
     Debug.Print "    Old Pos    = (" & vPos(0) * 1000# & ", " & vPos(1) * 1000# & ") mm"
    ' Move to right
     vPos(0) = vPos(0) + 0.01
     swView.Position = vPos
    vPos = swView.Position
     Debug.Print "    New Pos    = (" & vPos(0) * 1000# & ", " & vPos(1) * 1000# & ") mm"
    ' Redraw
     Dim rect() As Double
     swModelView.GraphicsRedraw rect
End Sub
```
