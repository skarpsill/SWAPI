---
title: "Insert Sheet Metal Gusset Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Sheet_Metal_Gusset_Feature_Example_VB.htm"
---

# Insert Sheet Metal Gusset Feature Example (VBA)

This example shows how to insert a sheet metal gusset feature and modify its data.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\SMGussetAPI.sldprt.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Inserts four sheet metal gussets.
 ' 2. Press F5 repeatedly and observe the gusset modifications.
 ' 3. Inspect the Immediate window for the flatten settings of all gussets.
 ' 4. Expand Flat-Pattern in the FeatureManager design tree, right-click
 '    Flat-Pattern(1), and click Unsuppress.
 ' 5. Observe the center marks and profiles of all the gussets in their
 '    flattened states.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim myFeature As SldWorks.Feature
 Dim myFeature1 As SldWorks.Feature
 Dim myFeature2 As SldWorks.Feature
 Dim myFeature3 As SldWorks.Feature
 Dim myFeature4 As SldWorks.Feature
 Dim swFeat As SldWorks.Feature
 Dim swFeatData As SldWorks.SMGussetFeatureData
 Dim boolstatus As Boolean
 Option Explicit
Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc

    boolstatus = Part.Extension.SelectByID2("", "FACE", -5.38403893476698E-02, 3.6701308754914E-03, 0.05530817474488, False, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("", "FACE", -1.77780871801474E-02, -3.07393226379986E-02, 3.41128529187245E-02, True, 0, Nothing, 0)

    ' Gusset #1 insertion parameters
     '1.  bOffset                    = True
     '2.  dOffset                    = 50 mm
     '3.  bFlipOffsetSide            = False
     '4.  profDimType                = 0 (indent depth dimensioning scheme)
     '5.  dIndentDepth               = 10 mm
     '6.  dLength                    = 0
     '7.  bUseAngle                  = False
     '8.  dHeight                    = 0
     '9   dAngle                     = 0
     '10. bFlipSides                 = False
     '11. dWidth                     = 10 mm
     '12. dThickness                 = 3 mm
     '13. bDraft                     = True
     '14. dDraftAngle                = 3 degrees
     '15. bInnerCornerFillet         = True
     '16. dInnerCornerFilletRadius   = 2 mm
     '17. bOuterCornerFillet         = True
     '18. dOuterCornerFilletRadius   = 1 mm
     '19. gussetType                 = 0 (rounded back)
     '20  bEdgeFillet                = False
     '21. dEdgeFilletRadius          = 0 mm
     '22. bOverrideDoc               = True
     '23. bShowProfile               = True
     '24. bShowCenter                = True

    Set myFeature = Part.FeatureManager.InsertSheetMetalGussetFeature3(True, 0.05, False, swSheetMetalGussetProfileDimType_IndentDepth, 0.01, 0, False, 0, 0, True, 0.01, 0.003, True, 3 * 0.0175, True, 0.002, True, 0.001, swSheetMetalRibGussetType_Rounded, False, 0, True, True, True)
     Part.ClearSelection2 True

    ' Gusset #2 insertion parameters (same as for Gusset #1 with the following exceptions)
     '2.  dOffset                = 30 mm
     '19. gussetType             = 1 (flat back)
     '20  bEdgeFillet            = True
     '21. dEdgeFilletRadius      = 1 mm

    ' Select faces
     boolstatus = Part.Extension.SelectByID2("", "FACE", -5.38403893476698E-02, 3.6701308754914E-03, 0.05530817474488, False, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("", "FACE", -1.77780871801474E-02, -3.07393226379986E-02, 3.41128529187245E-02, True, 0, Nothing, 0)

    Set myFeature1 = Part.FeatureManager.InsertSheetMetalGussetFeature3(True, 0.03, False, swSheetMetalGussetProfileDimType_IndentDepth, 0.01, 0, False, 0, 0, False, 0.01, 0.003, True, 3 * 0.0175, True, 0.002, True, 0.001, swSheetMetalRibGussetType_Flat, True, 0.001, True, True, True)
     Part.ClearSelection2 True

    ' Gusset #3 insertion parameters (same as for Gusset #1 with the following exceptions)
     '2.  dOffset                = 30 mm
     '4.  profDimType            = 1 (length + height dimensioning scheme)
     '5.  dIndentDepth           = 0 mm
     '6.  dLength                = 25 mm
     '7.  bUseAngle              = False
     '8.  dHeight                = 15 mm
     '9   dAngle                 = 0
     '10. bFlipSides             = False
     '19. gussetType             = 1 (flat back)
     '20  bEdgeFillet            = True
     '21. dEdgeFilletRadius      = 1 mm
    boolstatus = Part.Extension.SelectByID2("", "FACE", -5.38403893476698E-02, 3.6701308754914E-03, 0.05530817474488, False, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("", "FACE", -1.77780871801474E-02, -3.07393226379986E-02, 3.41128529187245E-02, True, 0, Nothing, 0)

    Set myFeature2 = Part.FeatureManager.InsertSheetMetalGussetFeature3(True, 0.03, False, swSheetMetalGussetProfileDimType_ProfileDimensions, 0, 0.025, False, 0.015, 0, False, 0.02, 0.003, True, 3 * 0.0175, True, 0.002, True, 0.001, swSheetMetalRibGussetType_Flat, True, 0.001, True, True, True)
     Part.ClearSelection2 True

    ' Gusset #4 insertion parameters (same as for Gusset #1 with the following exceptions)
     '2.  dOffset                = 30 mm
     '20  bEdgeFillet            = True
     '21. dEdgeFilletRadius      = 1 mm

     ' Select orientation and position references
     boolstatus = Part.Extension.SelectByID2("", "FACE", -5.38403893476129E-02, -2.24553153327633E-03, 0.087801420904043, True, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("", "FACE", -2.35965800548001E-02, -3.07393226379986E-02, 8.97844682415894E-02, True, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("Line1@Sketch6", "EXTSKETCHSEGMENT", -6.09049483400968E-03, -8.95139047397037E-02, 0, True, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("Point1@Sketch7", "EXTSKETCHPOINT", 1.80407947995604E-02, -7.62728416981986E-02, 0, True, 0, Nothing, 0)
    Set myFeature3 = Part.FeatureManager.InsertSheetMetalGussetFeature3(True, 0.03, False, swSheetMetalGussetProfileDimType_IndentDepth, 0.01, 0, False, 0, 0, False, 0.01, 0.003, True, 3 * 0.0175, True, 0.002, True, 0.001, swSheetMetalRibGussetType_Rounded, True, 0.001, True, True, True)
     Part.ClearSelection2 True
    Stop

    'Five modifications to gusset feature data:

        'a. Modify type, draft, and outer corner fillet options for gusset #1
         boolstatus = Part.Extension.SelectByID2("Sheet Metal Gusset1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
         Set swFeat = Part.SelectionManager.GetSelectedObject6(1, -1)

        Set swFeatData = swFeat.GetDefinition
         swFeatData.AccessSelections Part, Nothing
        swFeatData.GussetType = 1 'flat back
         swFeatData.DraftSideFaces = False
         swFeatData.FilletOuterCorners = False 'no outer corner fillet
         Debug.Print "Sheet Metal Gusset1 Flatten Settings"
         Debug.Print "  Override document property settings? " & swFeatData.OverrideDocSettings
         Debug.Print "  Show center marks? " & swFeatData.ShowCenter
         Debug.Print "  Show profile? " & swFeatData.ShowProfile

        swFeat.ModifyDefinition swFeatData, Part, Nothing
         swFeatData.ReleaseSelectionAccess

        Stop

        'b. Modify orientation reference of gusset #3
          boolstatus = Part.Extension.SelectByID2("Sheet Metal Gusset3", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
         Set swFeat = Part.SelectionManager.GetSelectedObject6(1, -1)

        Set swFeatData = swFeat.GetDefinition
         swFeatData.AccessSelections Part, Nothing
        boolstatus = Part.Extension.SelectByID2("Line1@Sketch6", "EXTSKETCHSEGMENT", -6.09049483400968E-03, -8.95139047397037E-02, 0, True, 0, Nothing, 0)
        Dim refLine As Variant
         Set refLine = Part.SelectionManager.GetSelectedObject6(1, -1)
         swFeatData.ReferenceLine = refLine
         swFeat.ModifyDefinition swFeatData, Part, Nothing

        Stop

        'c. Modify legs of gusset #2: select one bend face instead of two flat faces
          boolstatus = Part.Extension.SelectByID2("Sheet Metal Gusset2", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
         Set swFeat = Part.SelectionManager.GetSelectedObject6(1, -1)
        Set swFeatData = swFeat.GetDefinition
         swFeatData.AccessSelections Part, Nothing

        boolstatus = Part.Extension.SelectByID2("", "FACE", 0.03831148650454, -3.27672470662037E-02, 0.147978181958194, False, 0, Nothing, 0)
        Dim newBendFace As Variant
         Dim bendfaces(0 To 1) As Object
         Dim jj As Integer
         For jj = 0 To 1
            Set bendfaces(jj) = Part.SelectionManager.GetSelectedObject6(jj + 1, -1)
         Next jj
         newBendFace = bendfaces
         swFeatData.SupportingFaces = newBendFace
         Debug.Print "Sheet Metal Gusset2 Flatten Settings"
         Debug.Print "  Override document property settings? " & swFeatData.OverrideDocSettings
         Debug.Print "  Show center marks? " & swFeatData.ShowCenter
         Debug.Print "  Show profile? " & swFeatData.ShowProfile

        swFeat.ModifyDefinition swFeatData, Part, Nothing

        Stop

        'd. Modify reference position of gusset #3 - 3 mm away from vertex of hexagonal cut
          boolstatus = Part.Extension.SelectByID2("Sheet Metal Gusset3", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
         Set swFeat = Part.SelectionManager.GetSelectedObject6(1, -1)

        Set swFeatData = swFeat.GetDefinition
         swFeatData.AccessSelections Part, Nothing
        boolstatus = Part.Extension.SelectByID2("", "VERTEX", -5.38403893475499E-02, -1.00654290631334E-02, 0.205954465964501, False, 0, Nothing, 0)

        Dim refPoint As Variant
         Set refPoint = Part.SelectionManager.GetSelectedObject6(1, -1)
         swFeatData.ReferencePoint = refPoint
         Debug.Print "Sheet Metal Gusset3 Flatten Settings"
         Debug.Print "  Override document property settings? " & swFeatData.OverrideDocSettings
         Debug.Print "  Show center marks? " & swFeatData.ShowCenter
         Debug.Print "  Show profile? " & swFeatData.ShowProfile

        swFeat.ModifyDefinition swFeatData, Part, Nothing

        Stop

         'e. Modify type and inner corner fillet options for gusset #4
         boolstatus = Part.Extension.SelectByID2("Sheet Metal Gusset4", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
         Set swFeat = Part.SelectionManager.GetSelectedObject6(1, -1)
        Set swFeatData = swFeat.GetDefinition
         swFeatData.AccessSelections Part, Nothing

        swFeatData.GussetType = 0 'rounded back
         swFeatData.FilletInnerCorners = False 'no inner corner fillet
         Debug.Print "Sheet Metal Gusset4 Flatten Settings"
         Debug.Print "  Override document property settings? " & swFeatData.OverrideDocSettings
         Debug.Print "  Show center marks? " & swFeatData.ShowCenter
         Debug.Print "  Show profile? " & swFeatData.ShowProfile
        swFeat.ModifyDefinition swFeatData, Part, Nothing
         swFeatData.ReleaseSelectionAccess

End Sub
```
