---
title: "Insert Basic Dimension Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_and_Set_Basic_Dimension_Example_VBNET.htm"
---

# Insert Basic Dimension Example (VB.NET)

This example shows how to insert a DimXpert distance-between dimension.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Ensure that the part to open exists.
 ' 2. Reference the SOLIDWORKS DimXpert interop assembly:
  '    a. Right-click the project in Project Explorer.
 '    b. Click Add Reference.
 '    c. Click the Browse tab.
 '    d. Select install_dir\api\redist\swdimxpert.dll.
 '
 ' Postconditions: Inspect the graphics view and the DimXpertManager pane.
 '
  ' NOTE: Because the part is used elsewhere, do not save any changes.
  '----------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.swdimxpert
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim swConfig As Configuration
     Dim swDimXPertMgr As DimXpertManager
     Dim swDimXPertPart As DimXpertPart
     Dim swDimXPertDimOpt As DimXpertDimensionOption
     Dim dblDimXPertTextPos(2) As Double
     Dim varDimXPertTextPos As Object
     Dim boolstatus As Boolean
     Dim status As Integer, warnings As Integer

     Sub main()

         Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2017\Simulation Examples\actuator_casing.sldprt", 1, 0, "", status, warnings)
         swApp.ActivateDoc2("actuator_casing.sldprt", False, longstatus)
         Part = swApp.ActiveDoc

         Part.ShowNamedView2("*Isometric", 7)

         swConfig = Part.ConfigurationManager.ActiveConfiguration
         swDimXPertMgr = Part.Extension.DimXpertManager(swConfig.Name, True)
         swDimXPertPart = swDimXPertMgr.DimXpertPart
         swDimXPertDimOpt = swDimXPertPart.GetDimOption
         boolstatus = Part.Extension.SelectByID2("", "FACE", 0.0832566935649766, 0.0141096473029049, 0.0143449005094567, False, 0, Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("", "FACE", 0.0751728497303361, 0.000895850622406916, 0.0190499999998792, True, 0, Nothing, 0)
         dblDimXPertTextPos(0) = 0.083208
         dblDimXPertTextPos(1) = 0.045464
         dblDimXPertTextPos(2) = 0.019052
         varDimXPertTextPos = dblDimXPertTextPos
         swDimXPertDimOpt.TextPosition = varDimXPertTextPos
         boolstatus = swDimXPertPart.InsertBasicDimension(swDimXPertDimOpt)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
