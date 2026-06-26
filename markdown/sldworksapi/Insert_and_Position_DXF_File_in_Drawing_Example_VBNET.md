---
title: "Insert and Position DXF/DWG File in Drawing Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Position_DXF_File_in_Drawing_Example_VBNET.htm"
---

# Insert and Position DXF/DWG File in Drawing Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Const sDwgFileName As String = "DXF_file_path"

         Dim swModel As ModelDoc2
         Dim swModelView As ModelView
         Dim swDraw As DrawingDoc
         Dim swFeatMgr As FeatureManager
         Dim swFeat As Feature
         Dim swSketch As Sketch
         Dim swView As View
         Dim vPos As Object
         Dim bRet As Boolean
         Dim importData As ImportDxfDwgData

         swModel = swApp.ActiveDoc
         swModelView = swModel.ActiveView

         bRet = swModel.Extension.SelectByID2("Sheet1", "SHEET", 0.0#, 0.0#, 0, False, 0, Nothing, 0)

         swDraw = swModel
         swFeatMgr = swModel.FeatureManager
         importData = swApp.GetImportFileData(sDwgFileName)

         ' Unit
         importData.LengthUnit("") = swLengthUnit_e.swINCHES

         ' Position
         bRet = importData.SetPosition("", swDwgImportEntitiesPositioning_e.swDwgEntitiesCentered, 0, 0)

         ' Sheet scale
         bRet = importData.SetSheetScale("", 1.0#, 2.0#)

         ' Paper size
         bRet = importData.SetPaperSize("", swDwgPaperSizes_e.swDwgPaperAsize, 0.0#, 0.0#)

         ' Import method
         importData.ImportMethod("") = swImportDxfDwg_ImportMethod_e.swImportDxfDwg_ImportToExistingDrawing

         'Import file with importData
         swFeat = swFeatMgr.InsertDwgOrDxfFile2(sDwgFileName, importData)
         swSketch = swFeat.GetSpecificFeature2

         swView = swDraw.GetFirstView

         Do While Not swView Is  Nothing
             If swSketch Is swView.GetSketch Then
                 Exit Do
             End If
             swView = swView.GetNextView
         Loop

         vPos = swView.Position

         Debug.Print("File = " & swModel.GetPathName)
         Debug.Print("  Sketch       = " & swFeat.Name)
         Debug.Print("  View         = " & swView.Name)
         Debug.Print("    Old Pos    = (" & vPos(0) * 1000.0# & ", " & vPos(1) * 1000.0# & ") mm")

         ' Move to right
         vPos(0) = vPos(0) + 0.01
         swView.Position = vPos

         vPos = swView.Position
         Debug.Print("    New Pos    = (" & vPos(0) * 1000.0# & ", " & vPos(1) * 1000.0# & ") mm")

         ' Redraw
         Dim rect() As Double
         rect =  Nothing
         swModelView.GraphicsRedraw(rect)

     End Sub

     Public swApp As SldWorks

 End  Class
```
