---
title: "Get Data for Fillet Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Data_for_Simple_Fillet_Example_VBNET.htm"
---

# Get Data for Fillet Feature Example (VB.NET)

This example shows how to get the data for the selected fillet feature.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document with a simple fillet feature.
 ' 2. Select the simple fillet feature.
 ' 3. Open the Immediate window.
 ' 4. Run the macro.
 '
 ' Postconditions: Inspect the Immediate window.
 '---------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swSelMgr As SelectionMgr
         Dim swFeat As Feature
         Dim swFillet As SimpleFilletFeatureData2

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swFillet = swFeat.GetDefinition

         Debug.Print("File = " & swModel.GetPathName)
         Debug.Print("Feature = " & swFeat.Name)
         Debug.Print("   Constant width? " & swFillet.ConstantWidth)
         Debug.Print("   Curvature continuous? " & swFillet.CurvatureContinuous)
         Debug.Print("   Default radius = " & swFillet.DefaultRadius)
         Debug.Print("   Number of fillet items = " & swFillet.FilletItemsCount)
         Debug.Print("   Multiple radii? " & swFillet.IsMultipleRadius)
         Debug.Print("   Keep existing features? " & swFillet.KeepFeatures)
         Debug.Print("   Apply fillet to attachment edges? " & swFillet.OmitAttachedEdges)
         Debug.Print("   Overflow type = " & swFillet.OverflowType)
         Debug.Print("   Extend fillet to all affected parts? " & swFillet.PropagateFeatureToParts)
         Debug.Print("   Extend fillet to all tangent faces? " & swFillet.PropagateToTangentFaces)
         Debug.Print("   Reverse normal? " & swFillet.ReverseFaceNormal(0))
         Debug.Print("   Round fillet corners? " & swFillet.RoundCorners)
         Debug.Print("   Trim and attach to surfaces? " & swFillet.TrimAndAttachSurfaces)
         Debug.Print("   Type of fillet? " & swFillet.Type)
         Debug.Print "   Number of faces associated with this fillet = " & swFillet.GetFaceCount(swSimpleFilletWhichFaces_e.swSimpleFilletSingleRadius)

     End Sub

     Public swApp As SldWorks

 End  Class
```
