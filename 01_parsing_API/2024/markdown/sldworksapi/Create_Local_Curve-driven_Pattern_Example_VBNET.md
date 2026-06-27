---
title: "Create Local Curve-Driven Pattern Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Local_Curve-driven_Pattern_Example_VBNET.htm"
---

# Create Local Curve-Driven Pattern Example (VB.NET)

This example shows how to create a local curve-driven pattern feature.

```vb
'------------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified assembly document to open exists.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the assembly document.
 ' 2. Selects the component and edge for the
 '    local curve-driven pattern feature.
 ' 3. Creates a local curve-driven pattern feature.
 ' 4. Gets values and settings of the local curve-driven
 '    pattern feature.
 ' 5. Examine the Immediate window and graphics area.
 '
 ' NOTE: Because this assembly is used elsewhere, do not save
 ' changes.
 '------------------------------------------------------------------------------
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst

 Partial Class SolidWorksMacro

     Public Sub Main()

         Dim swModel As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim swFeatMgr As FeatureManager
         Dim swFeat As Feature
         Dim swLocalCurvePatternFeat As LocalCurvePatternFeatureData
         Dim fileName As String
         Dim status As Boolean
         Dim errors As Integer
         Dim warnings As Integer

         'Open assembly document
         fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\assem20.sldasm"
         swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

         'Select a component and an edge
         'for the local curve-driven pattern
         swModelDocExt = swModel.Extension
         status = swModelDocExt.SelectByID2("block20-1@assem20", "COMPONENT", 0, 0, 0, False, 1, Nothing, 0)
         status = swModelDocExt.SelectByID2("", "EDGE", 0.131144367102934, 0.0844607238593085, -0.124705856534547, True, 2, Nothing, 0)

         'Create local curve-driven pattern feature
         swFeatMgr = swModel.FeatureManager

         swLocalCurvePatternFeat = swFeatMgr.CreateDefinition(swFeatureNameID_e.swFmLocalCurvePattern)
         swLocalCurvePatternFeat.D1AlignmentMethod = 1
         swLocalCurvePatternFeat.D1CurveMethod = 1
         swLocalCurvePatternFeat.D1InstanceCount = 3
         swLocalCurvePatternFeat.D1IsEqualSpaced = True
         swLocalCurvePatternFeat.D1ReferencePoint = 1
         swLocalCurvePatternFeat.D1ReverseDirection = False
         swLocalCurvePatternFeat.D1Spacing = 0.05
         swLocalCurvePatternFeat.D2InstanceCount = 1
         swLocalCurvePatternFeat.D2IsEqualSpaced = False
         swLocalCurvePatternFeat.D2PatternSeedOnly = False
         swLocalCurvePatternFeat.D2ReverseDirection = False
         swLocalCurvePatternFeat.D2Spacing = 0.05
         swLocalCurvePatternFeat.Dir2Specified = False
         swFeat = swFeatMgr.CreateFeature(swLocalCurvePatternFeat)

         'Get local curve-driven pattern feature data
         swLocalCurvePatternFeat = swFeat.GetDefinition
         Debug.Print("Local curve-driven pattern properties: ")
         Debug.Print("  Number of components: " & swLocalCurvePatternFeat.GetPatternComponentCount)
         Debug.Print("  Number of skipped items: " & swLocalCurvePatternFeat.GetSkippedItemCount)
         Debug.Print("  Direction 1: ")
         Debug.Print("     Number of pattern instances: " & swLocalCurvePatternFeat.D1InstanceCount)
         Debug.Print("     Is direction flipped: " & swLocalCurvePatternFeat.D1ReverseDirection)
         Debug.Print("     Pattern instances equal spaced: " & swLocalCurvePatternFeat.D1IsEqualSpaced)
         Debug.Print("     Spacing for pattern instances: " & swLocalCurvePatternFeat.D1Spacing)
         Debug.Print("     Curve method: " & swLocalCurvePatternFeat.D1CurveMethod)
         Debug.Print("     Alignment method: " & swLocalCurvePatternFeat.D1AlignmentMethod)
         Debug.Print("  Direction 2:")
         Debug.Print("     Is Direction 2 specified: " & swLocalCurvePatternFeat.Dir2Specified)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
