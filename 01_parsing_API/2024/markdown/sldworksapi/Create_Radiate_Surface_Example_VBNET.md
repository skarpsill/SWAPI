---
title: "Create Radiate Surface Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Radiate_Surface_Example_VBNET.htm"
---

# Create Radiate Surface Feature Example (VB.NET)

This example shows how to create a radiate surface feature.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Verify that the specified document template exists.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a new model document with a feature extrusion.
 ' 2. Creates Boss-Extrude1 and Surface-Radiate1 in the graphics area and
 '    FeatureManager design tree.
 ' 3. Inspect the Immediate window.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim swSelMgr As SelectionMgr
     Dim swSelData As SelectData
     Dim swRadiate As SurfaceRadiateFeatureData
     Dim swFeat As Feature
     Dim swEnt As Edge
     Dim vRadEnt As Object
     Dim swRadDirEnt As Entity
     Dim i As Integer
     Dim boolStatus As Boolean

     Sub main()

         Part = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
         Part = swApp.ActiveDoc

         boolStatus = Part.Extension.SelectByID2("Front Plane", "PLANE", -0.0448901407839529, 0.0279954694016864, 0.00466820674117181, False, 0, Nothing, 0)
         Part.SketchManager.InsertSketch(True)
         Part.ClearSelection2(True)
         boolStatus = Part.Extension.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
         boolStatus = Part.Extension.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
         Dim vSkLines As Object
         vSkLines = Part.SketchManager.CreateCornerRectangle(-0.0555749908365768, 0.0329075527136081, 0, 0.0478203409524033, -0.0317145296545045, 0)
         Part.ClearSelection2(True)
         Part.SketchManager.InsertSketch(True)
         Part.ShowNamedView2("*Trimetric", 8)
         Part.SketchManager.InsertSketch(True)
         Part.ClearSelection2(True)
         boolStatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)

         Dim myFeature As Object
         myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.00254, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, True, True, True, 0, 0, False)

         boolStatus = Part.Extension.SelectByID2("", "EDGE", -0.0447337592343047, 0.0328467250718631, 0.00258132540182032, False, 2, Nothing, 0)
         boolStatus = Part.Extension.SelectByID2("", "EDGE", -0.0556265649287866, 0.0156695101210289, 0.0025672149453726, True, 2, Nothing, 0)
         boolStatus = Part.Extension.SelectByID2("", "EDGE", -0.0140113588298618, -0.0317157034173761, 0.00254079743683633, True, 2, Nothing, 0)
         boolStatus = Part.Extension.SelectByID2("", "EDGE", 0.047780958393389, -0.00542256709667299, 0.00256078163948814, True, 2, Nothing, 0)
         boolStatus = Part.Extension.SelectByID2("", "FACE", 0.0478203409524554, -0.00305747564971171, 0.000546558985774936, True, 1, Nothing, 0)

         Part.InsertRadiateSurface(0.0254, False, False)

         swSelMgr = Part.SelectionManager
         swSelData = swSelMgr.CreateSelectData

         boolStatus = Part.Extension.SelectByID2("Surface-Radiate1", "REFSURFACE", 0, 0, 0, False, 0, Nothing, 0)

         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swRadiate = swFeat.GetDefinition

         ' Get radiate surface data
         Debug.Print("File = " & Part.GetPathName)
         Debug.Print("  " & swFeat.Name)
         Debug.Print("    Distance: " & swRadiate.Distance * 1000.0# & " mm")
         Debug.Print("    Flip? " & swRadiate.Flip)
         Debug.Print("    Propagate to tangent faces? " & swRadiate.PropagateToTangentFaces)

         ' Roll back to get direction reference and radiated edges
         boolStatus = swRadiate.AccessSelections(Part, Nothing)
         swRadDirEnt = swRadiate.DirectionReference
         Part.ClearSelection2(True)

         vRadEnt = swRadiate.RadiatedEntities

         Debug.Print("Type as defined in swSelectType_e:)
         For i = 0 To swRadiate.GetRadiatedEntitiesCount - 1

             swEnt = vRadEnt(i)
             Debug.Print("    Radiated Entity(" & i & ") = " & swEnt.GetType)

         Next i

         swRadiate.ReleaseSelectionAccess()

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
