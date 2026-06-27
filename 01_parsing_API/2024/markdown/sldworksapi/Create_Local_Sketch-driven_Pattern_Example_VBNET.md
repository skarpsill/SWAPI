---
title: "Create Local Sketch-driven Pattern Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Local_Sketch-driven_Pattern_Example_VBNET.htm"
---

# Create Local Sketch-driven Pattern Example (VB.NET)

This example shows how to create a local sketch-driven pattern feature.

```
'------------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the assembly document.
' 2. Creates a sketch for the local sketch-driven
'    pattern.
' 3. Selects an assembly component and the just-created
'    sketch for the local sketch-driven pattern.
' 4. Creates local sketch-driven pattern.
' 5. Gets values and settings of the local sketch-driven pattern.
' 6. Examine the Immediate window.
'
' NOTE: Because this assembly is used elsewhere, do not save
' changes.
'------------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swSketchMgr As SketchManager
        Dim swSketchPoint As SketchPoint
        Dim swModelDocExt As ModelDocExtension
        Dim swFeatMgr As FeatureManager
        Dim swFeat As Feature
        Dim swLocalSketchPatternFeat As LocalSketchPatternFeatureData
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        'Open assembly document
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\assem1.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Create sketch
        swSketchMgr = swModel.SketchManager
        swSketchMgr.InsertSketch(True)
        swSketchPoint = swSketchMgr.CreatePoint(0.025, -0.05, 0.0#)
        swSketchPoint = swSketchMgr.CreatePoint(0.05, -0.075, 0.0#)
        swSketchPoint = swSketchMgr.CreatePoint(0.1, -0.05, 0.0#)
        swSketchMgr.InsertSketch(True)

        'Select a component and the just-created sketch
        'for the local sketch-driven pattern
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("TestPart1-1@assem1", "COMPONENT", 0, 0, 0, False, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, True, 16, Nothing, 0)

        'Insert local sketch-driven pattern
        swFeatMgr = swModel.FeatureManager
```

```vb
        swLocalSketchPatternFeat = swFeatMgr.CreateDefinition(swLocalSketchPatternReferencePoint_e.swFmLocalSketchPattern)
         swLocalSketchPatternFeat.ReferencePoint = 1 'Bounding box center
         swFeat = swFeatMgr.CreateFeature(swLocalSketchPatternFeat)

         'Get local sketch-driven pattern feature data
         swLocalSketchPatternFeat = swFeat.GetDefinition
         Debug.Print("Local sketch-driven pattern properties: ")
         Debug.Print("  Number of components: " & swLocalSketchPatternFeat.GetPatternComponentCount)
         Debug.Print("  Number of items skipped: " & swLocalSketchPatternFeat.GetSkippedItemCount)
         Debug.Print("  Type of reference point as defined in swLocalSketchPatternReferencePoint_e: " & swLocalSketchPatternFeat.ReferencePoint)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
