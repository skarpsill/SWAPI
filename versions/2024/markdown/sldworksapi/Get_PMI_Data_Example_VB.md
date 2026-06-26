---
title: "Get PMI Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_PMI_Data_Example_VB.htm"
---

# Get PMI Data Example (VBA)

This example shows how to get Product and Manufacturing Information (PMI) from a Step 242 file.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a Step 242 file that contains PMI annotations.
 ' 2. Open an Immediate window.
 ' 3. Add breakpoints as needed and press F8 to walk through the macro.
 '
 ' Postconditions:
 ' Inspect the Immediate window for PMI annotations, if available.
 '----------------------------------------------------------------------------
 Option Explicit
 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swAnnotation As SldWorks.Annotation
 Dim swPMIDatumData As SldWorks.PMIDatumData
 Dim swPMIDatumFeature As SldWorks.PMIDatumFeature
 Dim swPMIDatumTarget As SldWorks.PMIDatumTarget
 Dim swPMIDataDim As SldWorks.PMIDimensionData
 Dim swPMIDataDimItem As SldWorks.PMIDimensionItem
 Dim swPMIDataGtol As SldWorks.PMIGtolData
 Dim swPMIGtolBoxData As SldWorks.PMIGtolBoxData
 Dim swPMIFrameData As SldWorks.PMIFrameData
 Dim swPMIGtolFrameDatum As SldWorks.PMIGtolFrameDatum
 Dim IAnnoPMIType As Long
 Dim iAnnoCnt As Long
 Dim arrAnnotation As Variant
 Dim dText As String
 Dim i As Long
 Dim j As Long
 Dim k As Long
 Dim l As Long
 Dim IAnnoType As Long

 Sub main()
     Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension

    iAnnoCnt = swModelDocExt.GetAnnotationCount()

    If iAnnoCnt > 0 Then
     arrAnnotation = swModelDocExt.GetAnnotations()

        For i = LBound(arrAnnotation) To UBound(arrAnnotation)

            Set swAnnotation = arrAnnotation(i)

            IAnnoType = swAnnotation.GetType()

             IAnnoPMIType = swAnnotation.GetPMIType

            Select Case IAnnoType
                 Case 1
                     Debug.Print "Annotation: Thread"

                Case 2
                     Debug.Print "Annotation: Datum Tag " & swAnnotation.GetName

                    If IAnnoPMIType = 2 Then

                         Set swPMIDatumData = swAnnotation.GetPMIData

                        Debug.Print "PMI datum data"

                         dText = ""

                        If swPMIDatumData.GetDatumType = SwConst.swPMIDatumType_e.swPMIDatumType_DatumFeature Then
                             dText = "swPMIDatumType_e.swPMIDatumType_DatumFeature"

                            'Get IPMIDatumFeature

                             Set swPMIDatumFeature = swPMIDatumData.GetDatumFeature
                             Debug.Print " Datum feature"
                             Debug.Print "  Label: " & swPMIDatumFeature.Label
                             Debug.Print "  Leader anchor style as defined in swPMIDatumAnchorStyle_e: " & swPMIDatumFeature.LeaderAnchorStyle
                             Debug.Print "  Leader bend length: " & swPMIDatumFeature.LeaderBendLength
                             Debug.Print "  Datum shape as defined in swPMIDatumShape_e: " & swPMIDatumFeature.Shape
                             Debug.Print "  Datum text: " & swPMIDatumFeature.Text
                        End If

                        If swPMIDatumData.GetDatumType = SwConst.swPMIDatumType_e.swPMIDatumType_DatumTarget Then
                             dText = "swPMIDatumType_e.swPMIDatumType_DatumTarget"

                            'Get IPMIDatumTarget

                             Set swPMIDatumTarget = swPMIDatumData.GetDatumTarget

                            Debug.Print " Datum target"
                             Debug.Print "  Area style as defined in swPMIDatumTargetAreaStyle_e: " & swPMIDatumTarget.AreaStyle
                             Debug.Print "  Diameter: " & swPMIDatumTarget.Diameter
                             Debug.Print "  Height: " & swPMIDatumTarget.Height
                             Debug.Print "  Movable style as defined in swPMIDatumTargetMovableStyle_e: " & swPMIDatumTarget.MovableStyle
                             Debug.Print "  Symbol style as defined in swPMIDatumTargetSymbolStyle_e: " & swPMIDatumTarget.SymbolStyle
                             Debug.Print "  Width: " & swPMIDatumTarget.Width
                        End If

                         Debug.Print ""

                    ElseIf IAnnoPMIType = 0 Then
                         If swPMIDatumData Is Nothing Then
                             Debug.Print "   No PMI data"
                         Else
                             Debug.Print "   PMIDatumData object returned In Error"
                         End If
                     Else
                         Debug.Print "   Wrong PMI data type"
                     End If

                Case 3
                     Debug.Print "Annotation: Datum Target Symbol"
                 Case 4
                     Debug.Print "Annotation: Display Dimension " & swAnnotation.GetName

                    If IAnnoPMIType = 1 Then

                         Set swPMIDataDim = swAnnotation.GetPMIData

                        If Not swPMIDataDim Is Nothing Then

                            For k = 0 To swPMIDataDim.GetDimensionItemCount - 1
                                 Set swPMIDataDimItem = swPMIDataDim.GetDimensionItemAtIndex(k)

                                Debug.Print "  Dimension item " & k
                                 Debug.Print "    Text: " & swPMIDataDim.DimensionText
                                 Debug.Print "    Instance count: " & swPMIDataDimItem.InstanceCount
                                 Debug.Print "    Tolerance type as defined in swTolType_e: " & swPMIDataDimItem.TolType
                                 Debug.Print "    Value: " & swPMIDataDimItem.Value
                                 Debug.Print "    Value precision: " & swPMIDataDimItem.ValuePrecision
                                 Debug.Print "    Units: " & swPMIDataDimItem.Unit
                                 Debug.Print "    Minimum tolerance: " & swPMIDataDimItem.MinVariation
                                 Debug.Print "    Maximum tolerance: " & swPMIDataDimItem.MaxVariation
                                 Debug.Print "    Tolerance precision: " & swPMIDataDimItem.TolerancePrecision
                                 Debug.Print "    Symbol as defined in swDimensionSymbol_e: " & swPMIDataDimItem.Symbol
                                 Debug.Print "    Additional symbol as defined in swToleranceZoneModifier_e: " & swPMIDataDimItem.AdditionalSymbol
                                 Debug.Print "    Prefix: " & swPMIDataDimItem.Prefix
                                 Debug.Print "    Suffix: " & swPMIDataDimItem.Suffix
                                  Debug.Print "    Callout: " & swPMIDataDimItem.CalloutText
                                 Debug.Print ""
                             Next
                         End If

                    ElseIf (IAnnoPMIType = 0) Then
                         If swPMIDataDim Is Nothing Then
                             Debug.Print "   No PMI data"
                         Else
                             Debug.Print "   PMIDimensionData object returned in error"
                         End If
                     Else
                         Debug.Print "   Wrong PMI data type"
                     End If
                 Case 5
                      Debug.Print "Annotation: Gtol " & swAnnotation.GetName

                     If IAnnoPMIType = 3 Then

                         Set swPMIDataGtol = swAnnotation.GetPMIData

                        If Not swPMIDataGtol Is Nothing Then

                            Debug.Print "  Is composite? " & swPMIDataGtol.IsComposite
                             Debug.Print "  Text: " & swPMIDataGtol.GetText
                             Debug.Print "  Text below frames: " & swPMIDataGtol.GetTextBelowFrames
                             Debug.Print "  Instance count: " & swPMIDataGtol.InstanceCount
                             Debug.Print "  Leader location as defined in swPMILeaderLocation_e: " & swPMIDataGtol.LeaderLocation
                             Debug.Print "  Leader modifier as defined in swPMILeaderModifier_e: " & swPMIDataGtol.LeaderModifier
                             Debug.Print "  Leader style as defined in swPMILeaderStyle_e: " & swPMIDataGtol.LeaderStyle
                             Debug.Print "  Leader type as defined in swPMILeaderType_e: " & swPMIDataGtol.LeaderType

                            Dim iFrameCount As Integer
                             iFrameCount = swPMIDataGtol.GetFrameCount

                            Debug.Print "  Frame count is " & iFrameCount

                            If iFrameCount = 0 Then
                                 Debug.Print "Gtol frame count is zero - API error"
                             End If

                            For j = 0 To swPMIDataGtol.GetFrameCount - 1

                                 Set swPMIFrameData = swPMIDataGtol.GetFrameAtIndex(j)
                                 If Not swPMIFrameData Is Nothing Then

                                    Debug.Print "  Gtol frame " & j & " data"
                                     Debug.Print "    Geometric characteristic as defined in swGeometricCharacteristic_e: " & swPMIFrameData.GeometricCharacteristic
                                     Debug.Print "    Frame number: " & swPMIFrameData.FrameNumber

                                 'Get IPMIGtolBoxData

                                For k = 0 To swPMIFrameData.GetGtolBoxCount - 1
                                     Set swPMIGtolBoxData = swPMIFrameData.GetGtolBoxAtIndex(k)
                                     Debug.Print "    Gtol box " & k
                                     Debug.Print "      Material modifier as defined in swMaterialModifier_e: " & swPMIGtolBoxData.MaterialModifier
                                     Debug.Print "      Tolerance: " & swPMIGtolBoxData.TolValue
                                     Debug.Print "      Units as defined in swPMIUnit_e: " & swPMIGtolBoxData.Unit
                                     Debug.Print "      Tolerance zone modifier as defined in swToleranceZoneModifier_e: " & swPMIGtolBoxData.ToleranceZoneModifier
                                     Debug.Print "      Tolerance per unit area type as defined in swPMITolPerUnitAreaType_e: " & swPMIGtolBoxData.TolerancePerUnitType
                                     Debug.Print "      Tolerance 1 per unit area value: " & swPMIGtolBoxData.TolerancePerUnitValue1
                                     Debug.Print "      Tolerance 2 per unit area value: " & swPMIGtolBoxData.TolerancePerUnitValue2
                                  Next

                                'Get IPMIGtolFrameDatum

                                For l = 0 To swPMIFrameData.GetGtolDatumCount - 1
                                     Set swPMIGtolFrameDatum = swPMIFrameData.GetGtolDatumAtIndex(l)
                                     Debug.Print "    Gtol frame datum " & l
                                     Debug.Print "      Datum: " & swPMIGtolFrameDatum.Datum
                                     Debug.Print "      Material modifier as defined in swMaterialModifier_e: " & swPMIGtolFrameDatum.DatumModifier
                                     Debug.Print "      Material modifier value if present: " & swPMIGtolFrameDatum.DatumModifierValue
                                     Debug.Print "      First linked datum: " & swPMIGtolFrameDatum.DatumLinked1
                                     Debug.Print "      Material modifier of first linked datum as defined in swMaterialModifier_e: " & swPMIGtolFrameDatum.DatumLinkedModifier1
                                     Debug.Print "      Value, if present, of material modifier of first linked datum: " & swPMIGtolFrameDatum.DatumLinkedModifierValue1
                                     Debug.Print "      Second linked datum: " & swPMIGtolFrameDatum.DatumLinked2
                                     Debug.Print "      Material modifier of second linked datum as defined in swMaterialModifier_e: " & swPMIGtolFrameDatum.DatumLinkedModifier2
                                     Debug.Print "      Value, if present, of material modifier of second linked datum: " & swPMIGtolFrameDatum.DatumLinkedModifierValue2
                                 Next
                                 Else
                                     Debug.Print "Gtol frame retrieval error"
                                 End If

                            Next

                        End If

                     ElseIf IAnnoPMIType = 0 Then
                         If swPMIDataGtol Is Nothing Then
                             Debug.Print "   No PMI data"
                         Else
                             Debug.Print "   PMIGtolData object returned in error"
                         End If
                      Else
                         Debug.Print "   Wrong PMI data type"
                      End If

                Case 6
                      Debug.Print "Annotation: Note"

                Case 7
                      Debug.Print "Annotation: SF Symbol"

                Case 8
                      Debug.Print "Annotation: Weld Symbol"

                Case 9
                      Debug.Print "Annotation: Custom Symbol"

                Case 10
                      Debug.Print "Annotation: Dowel Symbol"

                Case 11
                      Debug.Print "Annotation: Leader"

                Case 12
                      Debug.Print "Annotation: Block"

                Case 13
                      Debug.Print "Annotation: Centermark symbol"

                Case 14
                      Debug.Print "Annotation: Table"

                Case 15
                      Debug.Print "Annotation: Centerline"

                Case 16
                      Debug.Print "Annotation: Datum Origin"

             End Select
         Next

    End If
 End Sub
```
