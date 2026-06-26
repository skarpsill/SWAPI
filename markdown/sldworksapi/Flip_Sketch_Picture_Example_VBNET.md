---
title: "Flip Sketch Picture Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Flip_Sketch_Picture_Example_VBNET.htm"
---

# Flip Sketch Picture Example (VB.NET)

This example shows how to flip a sketch picture.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified document template exists.
 ' 2. Copy an image file (i.e., .bmp, .gif, .jpg, .jpeg, .tif, .wmf) to
 '    c:\temp.
 ' 3. Replace image_file in the ISketchManager::InsertSketchPicture parameter
 '    with the name of the copied file.
 ' 4. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a new model document.
 ' 2. Creates Sketch1 and Sketch Picture1 in the graphics area and the
 '    FeatureManager design tree.
 ' 3. Selects Sketch Picture1 and flips it top to bottom.
 ' 4. Inspect the Immediate window.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swFeat As Feature
     Dim swSketchPicture As SketchPicture
     Dim swSelMgr As SelectionMgr
     Dim boolstatus As Boolean
     Dim width As Double
     Dim height As Double
     Dim x As Double
     Dim y As Double
     Dim angle As Double

     Sub main()

         swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2020\templates\Part.prtdot", 0, 0, 0)
         swModel = swApp.ActiveDoc

         swSelMgr = swModel.SelectionManager
         swModel.SketchManager.InsertSketch(True)
         swSketchPicture = swModel.SketchManager.InsertSketchPicture2("c:\temp\image_file", False)
         swModel.SketchManager.InsertSketch(True)

         boolstatus = swModel.Extension.SelectByID2("Sketch Picture1", "SKETCHBITMAP", 0, 0, 0, False, 0, Nothing, 0)
         swFeat = swSelMgr.GetSelectedObject6(1, -1)

         Debug.Print("Feature name = " & swFeat.Name)

         boolstatus = swSketchPicture.Flip(False)
         Debug.Print("  Sketch picture flipped? " & swSketchPicture.Flipped)

         swSketchPicture.GetSize(width, height)
         Debug.Print("  Width: " & width * 1000 & " mm")
         Debug.Print("  Height: " & height * 1000 & " mm")

         angle = swSketchPicture.Angle
         '1 radian = 180º/p = 57.295779513º or approximately 57.3º
         Debug.Print("  Angle: " & angle * 57.3 & " degrees")

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
