---
title: "Insert General Tolerance Table Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_General_Tolerance_Table_Example_VBNET.htm"
---

# Insert General Tolerance Table Example (VB.NET)

This example shows how to create a general tolerance table annotation.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part.
 ' 2. Ensure that the specified table template exists.
 ' 3. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a general tolerance table annotation.
  ' 2. Inspect the Immediate window, the graphics area, and the Tables folder
 '    of the FeatureManager design tree.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks

 Partial Class SolidWorksMacro

     Public Sub main()

         Dim Part As ModelDoc2
         Dim gttAnno As GeneralToleranceTableAnnotation
         Dim gttFeat As GeneralToleranceTableFeature
         Dim feat As Feature
         Dim mde As ModelDocExtension
         Dim boolstatus As Boolean

         Part = swApp.ActiveDoc
         mde = Part.Extension
         gttAnno = mde.InsertGeneralToleranceTableAnnotation("c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\bom-standard.sldbomtbt", 481, 163)
         gttFeat = gttAnno.GeneralToleranceTableFeature
         feat = gttFeat.GetFeature
         Debug.Print("Created " & feat.Name)
         boolstatus = Part.EditRebuild3()

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
