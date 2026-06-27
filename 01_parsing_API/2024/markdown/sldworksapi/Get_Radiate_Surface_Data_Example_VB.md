---
title: "Create Radiate Surface Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Radiate_Surface_Data_Example_VB.htm"
---

# Create Radiate Surface Feature Example (VBA)

This example shows how to create a radiate surface feature.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified document template exists.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a new model document with a feature extrusion.
 ' 2. Creates Boss-Extrude1  and Surface-Radiate1 in the graphics area and
 '    FeatureManager design tree.
 ' 3. Inspect the Immediate window.
 '----------------------------------------------------------------------------
Dim swApp                As SldWorks.SldWorks
 Dim Part                 As SldWorks.ModelDoc2
 Dim swSelMgr             As SldWorks.SelectionMgr
 Dim swSelData            As SldWorks.SelectData
 Dim swRadiate            As SldWorks.SurfaceRadiateFeatureData
 Dim swFeat               As SldWorks.Feature
 Dim swEnt                As SldWorks.Entity
 Dim vRadEnt              As Variant
 Dim swRadDirEnt          As SldWorks.Entity
 Dim i                    As Long
 Dim boolStatus           As Boolean
 Option Explicit
Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
     Set Part = swApp.ActiveDoc

     boolStatus = Part.Extension.SelectByID2("Front Plane", "PLANE", -4.48901407839529E-02, 2.79954694016864E-02, 4.66820674117181E-03, False, 0, Nothing, 0)
     Part.SketchManager.InsertSketch True
     Part.ClearSelection2 True
     boolStatus = Part.Extension.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
     boolStatus = Part.Extension.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
     Dim vSkLines As Variant
     vSkLines = Part.SketchManager.CreateCornerRectangle(-5.55749908365768E-02, 3.29075527136081E-02, 0, 4.78203409524033E-02, -3.17145296545045E-02, 0)
     Part.ClearSelection2 True
     Part.SketchManager.InsertSketch True
     Part.ShowNamedView2 "*Trimetric", 8
     Part.SketchManager.InsertSketch True
     Part.ClearSelection2 True
     boolStatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)

    Dim myFeature As Object
     Set myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.00254, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)

    boolStatus = Part.Extension.SelectByID2("", "EDGE", -4.47337592343047E-02, 3.28467250718631E-02, 2.58132540182032E-03, False, 2, Nothing, 0)
     boolStatus = Part.Extension.SelectByID2("", "EDGE", -5.56265649287866E-02, 1.56695101210289E-02, 2.5672149453726E-03, True, 2, Nothing, 0)
     boolStatus = Part.Extension.SelectByID2("", "EDGE", -1.40113588298618E-02, -3.17157034173761E-02, 2.54079743683633E-03, True, 2, Nothing, 0)
     boolStatus = Part.Extension.SelectByID2("", "EDGE", 0.047780958393389, -5.42256709667299E-03, 2.56078163948814E-03, True, 2, Nothing, 0)
     boolStatus = Part.Extension.SelectByID2("", "FACE", 4.78203409524554E-02, -3.05747564971171E-03, 5.46558985774936E-04, True, 1, Nothing, 0)

    Part.InsertRadiateSurface 0.0254, False, False

    Set swSelMgr = Part.SelectionManager
     Set swSelData = swSelMgr.CreateSelectData

    boolStatus = Part.Extension.SelectByID2("Surface-Radiate1", "REFSURFACE", 0, 0, 0, False, 0, Nothing, 0)

    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swRadiate = swFeat.GetDefinition

    ' Get radiate surface data
     Debug.Print "File = " & Part.GetPathName
     Debug.Print "  " & swFeat.Name
     Debug.Print "    Distance: " & swRadiate.Distance * 1000# & " mm"
     Debug.Print "    Flip? " & swRadiate.Flip
     Debug.Print "    Propagate to tangent faces? " & swRadiate.PropagateToTangentFaces
    ' Roll back to get direction reference and radiated edges
     boolStatus = swRadiate.AccessSelections(Part, Nothing)
     Set swRadDirEnt = swRadiate.DirectionReference
     Part.ClearSelection2 True
    vRadEnt = swRadiate.RadiatedEntities
    Debug.Print "Type as defined in swSelectType_e:"
     For i = 0 To swRadiate.GetRadiatedEntitiesCount - 1
        Set swEnt = vRadEnt(i)
         Debug.Print "  Radiated entity(" & i & ") = " & swEnt.GetType
    Next i
    swRadiate.ReleaseSelectionAccess

 End Sub
```
