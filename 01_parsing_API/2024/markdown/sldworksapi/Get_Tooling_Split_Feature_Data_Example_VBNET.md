---
title: "Get Tooling Split Feature Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Tooling_Split_Feature_Data_Example_VBNET.htm"
---

# Get Tooling Split Feature Data Example (VB.NET)

This example shows how to get tooling split feature data.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document that contains a Tooling Split1 feature.
 ' 2. Select Tooling Split1 in the FeatureManager design tree.
 ' 3. Open an Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swSelMgr As SelectionMgr
     Dim swFeat As Feature
     Dim swToolingSplitFeatData As ToolingSplitFeatureData
     Dim bod As Body2
     Dim bRet As Boolean
     Dim i As Integer
     Dim cavSurf As Object
     Dim coreSurf As Object
     Dim partSurf As Object

     Sub main()

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swToolingSplitFeatData = swFeat.GetDefinition

         Debug.Print("File = " & swModel.GetPathName)
         Debug.Print("  " & swFeat.Name)
         Debug.Print("    Draft angle: " & swToolingSplitFeatData.Angle)
         Debug.Print("    Depth of block in direction 1: " & swToolingSplitFeatData.Depth(0))
         Debug.Print("    Depth of block in direction 2: " & swToolingSplitFeatData.Depth(1))
         Debug.Print("    Interlock surface? " & swToolingSplitFeatData.InterlockSurface)

         bRet = swToolingSplitFeatData.AccessSelections(swModel, Nothing)

         Debug.Print("    Cavity surfaces:")
         Debug.Print("    Count: " & swToolingSplitFeatData.GetCavitySurfacesCount)
         cavSurf = swToolingSplitFeatData.CavitySurfaces
         For i = 0 To swToolingSplitFeatData.GetCavitySurfacesCount - 1
             bod = cavSurf(i)
             Debug.Print("      " & bod.Name)
         Next
         Debug.Print("    Core surfaces:")
         Debug.Print("    Count: " & swToolingSplitFeatData.GetCoreSurfacesCount)
         coreSurf = swToolingSplitFeatData.CoreSurfaces
         For i = 0 To swToolingSplitFeatData.GetCoreSurfacesCount - 1
             bod = coreSurf(i)
             Debug.Print("      " & bod.Name)
         Next
         Debug.Print("    Parting surfaces:")
         Debug.Print("    Count: " & swToolingSplitFeatData.GetPartingSurfacesCount)
         partSurf = swToolingSplitFeatData.PartingSurfaces
         For i = 0 To swToolingSplitFeatData.GetPartingSurfacesCount - 1
             bod = partSurf(i)
             Debug.Print("      " & bod.Name)
         Next

         swToolingSplitFeatData.ReleaseSelectionAccess()

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
