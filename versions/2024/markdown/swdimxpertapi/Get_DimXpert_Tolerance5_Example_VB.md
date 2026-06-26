---
title: "Get DimXpert Tolerance5 Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Tolerance5_Example_VB.htm"
---

# Get DimXpert Tolerance5 Example (VBA)

This example shows how to build a part and get attributes for the DimXpertkadov_tag{{</spaces>}}Concentricity
geometric tolerance annotation.

kadov_tag{{<spaces>}}

```vb
'-----------------------------------------------------------------------------
' Preconditions: kadov_tag{{<spaces>}}
'  1. Open public_documents\samples\tutorial\api\cover_with_dimensions.sldprt.
' kadov_tag{{<spaces>}} 2. Open the DimXpert toolbar from View > Toolbars.
'
' Create concentricity geometric tolerance:
'  kadov_tag{{<spaces>}}1. Click Datum of the DimXpert tool bar.
' kadov_tag{{<spaces>}} 2. Click Boss1 (front extrusion).
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}} 3. Click to place the annotation.
'  kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}4. Click the green check mark to accept Datum A.
' kadov_tag{{<spaces>}} 5. Click Geometric Tolerance of the DimXpert toolbar.
' kadov_tag{{<spaces>}} 6. kadov_tag{{</spaces>}}In the Geometric Tolerance Properties dialog:
' kadov_tag{{<spaces>}}    a. Select Concentricity in the Symbol dropdown.
' kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}b. Click Tolerance 1.
' kadov_tag{{<spaces>}}    c. Click Diameter on the toolbar at the top of the dialog.
' kadov_tag{{<spaces>}}    d. Type A in Primary.
' kadov_tag{{<spaces>}} 7. Click the inside face of Simple Hole2.
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}} 8. Click to place the annotation.
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}} 9. Click OK to close the Geometric Tolerance Properties dialog.
' 10. In the DimXpertManager tab of the Management Panel, expand Simple Hole2.
' kadov_tag{{<spaces>}}11. Observe the following Dimxpert annotation: kadov_tag{{</spaces>}}Concentricity1
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}12. Ensure that the SOLIDWORKS DimXpert type library is loaded
'     in Tools > References.
' kadov_tag{{<spaces>}}13. Ensure that the Microsoft Scripting Runtime library is loaded
'     in Tools > References.
'
' Postconditions:
'  kadov_tag{{<spaces>}}1. Writes the output ton c:\temp\dimXpertInfo.txt.
'  kadov_tag{{<spaces>}}2. Inspect the Immediate window.
'
' kadov_tag{{<spaces>}}NOTE: Because the part is used elsewhere, do not save changes.
'--------------------------------------------------
Option Explicit
Dim strs As New Collection
Dim dimXpertPart As SwDimXpert.dimXpertPart
Sub Main()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swapp As SldWorks.SldWorks
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swapp = Application.SldWorks
kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Dim swModelDoc As SldWorks.ModelDoc2
kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Set swModelDoc = swapp.ActiveDoc
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If swModelDoc Is Nothing Then
kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim f As New FileSystemObject
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim textStr As TextStream
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set textStr = f.CreateTextFile("C:\temp\dimXpertInfo.txt", True)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If textStr Is Nothing Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "Error creating temp file."
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call log("Starting DimXpert log...", textStr)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call retrieve_info_text(swapp, textStr)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}textStr.Close
End Sub
Private Sub log(text As String, textStr As TextStream)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print text
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}textStr.WriteLine (text)
End Sub
Private Sub retrieve_info_text(swapp As SldWorks.SldWorks, textStr As TextStream)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim dimXpertMgr As SldWorks.DimXpertManager
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set dimXpertMgr = swapp.IActiveDoc2.Extension.DimXpertManager(swapp.IActiveDoc2.IGetActiveConfiguration().Name, True)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call log("Model: " & swapp.IActiveDoc2.GetPathName, textStr)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim dimXpertPartObj As dimXpertPart
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set dimXpertPartObj = dimXpertMgr.dimXpertPart
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set dimXpertPart = dimXpertPartObj
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vAnnotations As Variant
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}vAnnotations = dimXpertPart.GetAnnotations()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call log("------------------------", textStr)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call log("Annotations...", textStr)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call log("------------------------", textStr)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim annotationTemp As DimXpertAnnotation
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim annotationIndex As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}For annotationIndex = 0 To UBound(vAnnotations)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set annotationTemp = vAnnotations(annotationIndex)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim AnnotationDataText As Collection
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set AnnotationDataText = AnnotationData(annotationTemp)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim annotationTextIndex As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For annotationTextIndex = 1 To AnnotationDataText.Count
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call log(AnnotationDataText(annotationTextIndex), textStr)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Next
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
End Sub
Public Function AnnotationData(annotation As DimXpertAnnotation) As Collection
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim annoType As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'general info
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call GeneralInfo(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}annoType = annotation.Type
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If annoType = swDimXpertDatum Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call DatumData(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertGeoTol_Position Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call PositionData(annotation)
kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertGeoTol_CompositePosition Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call CompositePositionData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertGeoTol_Symmetry Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call SymmetryData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertGeoTol_Concentricity Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call ConcentricityData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertGeoTol_LineProfile Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call LineProfileData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertGeoTol_CompositeLineProfile Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call CompositeLineProfileData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertGeoTol_SurfaceProfile Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call SurfaceProfileData(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertGeoTol_CompositeSurfaceProfile Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call CompositeSurfaceProfileData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertGeoTol_Angularity Or annoType = swDimXpertGeoTol_Parallelism Or annoType = swDimXpertGeoTol_Perpendicularity Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call OrientationData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertGeoTol_TotalRunout Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call TotalRunoutData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertGeoTol_CircularRunout Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call CircularRunoutData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertGeoTol_Flatness Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call FlatnessData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertGeoTol_Circularity Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call CircularityData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertGeoTol_Cylindricity Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call CylindricityData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertGeoTol_Straightness Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call StraightnessData(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertGeoTol_Tangency Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call TangencyData(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Else kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' any of the dimension tolerance types
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call DimensionToleranceData(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set AnnotationData = strs
End Function
Private Sub Clear(strs As Collection)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim n As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Remove (strs.Count)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If Not strs.Count = 0 Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call Clear(strs)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
End Sub
Private Sub GeneralInfo(annotation As DimXpertAnnotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim annoType As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim modelObj As Object
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim modelFeature As SldWorks.feature
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If Not strs.Count = 0 Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call Clear(strs)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Name: " + annotation.Name)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}annoType = annotationTypeNameFromObject(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Type: " + annoType)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Display Entity: " + DisplayEntity(annotation))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set modelObj = annotation.GetModelFeature
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set modelFeature = modelObj
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If Not (modelFeature Is Nothing) Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("ModelFeature: " + modelFeature.Name + " (" + modelFeature.GetTypeName2() + ")")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
End Sub
Private Sub DatumData(annotation As DimXpertDatum)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the datum letter
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Datum Letter: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}" + annotation.Identifier)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
Private Sub PositionData(annotation As DimXpertPositionTolerance)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim I As Double, J As Double, K As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim enabled As Boolean, value As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Position Tolerance Compartment:")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the shape of the tolerance zone
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Zone Type: " + PositionZoneType(annotation.zoneType))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the zone vector if the tolerance zone is planar
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If annotation.zoneType = swDimXpertPositionZoneType_PlanarPosition Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetPlanarZoneVector(I, J, K)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Direction: " + FormatVector(I, J, K))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the material condition modifer applied to feature
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Modifier: " + mcmStr(annotation.modifier))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the projected tolerance zone when specified
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = annotation.GetProjectedZone(enabled, value)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call FormatProjectedZone(enabled, value)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
Private Sub CompositePositionData(annotation As DimXpertCompositePositionTolerance)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim I As Double, J As Double, K As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim enabled As Boolean, value As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Composite Position Tolerance Compartment")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the shape of the tolerance zone
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Zone Type: " + PositionZoneType(annotation.zoneType))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the zone vector when the zone is planar
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If annotation.zoneType = swDimXpertPositionZoneType_PlanarPosition Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetPlanarZoneVector(I, J, K)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Direction: " + FormatVector(I, J, K))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the material condition modifer
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Modifier: " + mcmStr(annotation.modifier))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the projected tolerance zone when specified
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = annotation.GetProjectedZone(enabled, value)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call FormatProjectedZone(enabled, value)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the datum reference frame for the pattern location
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the datum reference frame for the feature to feature location
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Composite datums:")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Repeat Primary: " + IIf(annotation.PrimaryInLowerTier, "True", "False"))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Repeat Secondary: " + IIf(annotation.SecondaryInLowerTier, "True", "False"))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Repeat Tertiary: " + IIf(annotation.TertiaryInLowerTier, "True", "False"))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
Private Sub SymmetryData(annotation As DimXpertSymmetryTolerance)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim I As Double, J As Double, K As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Symmetry Tolerance Compartment")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the material condition modifer applied to feature
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Modifier: " + mcmStr(annotation.modifier))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the direction of the planar zone
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = annotation.GetZoneDirection(I, J, K)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Planar Zone Direction: " + FormatVector(I, J, K))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
End Sub
Private Sub ConcentricityData(annotation As DimXpertConcentricityTolerance)
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Concentricity Tolerance Compartment")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the material condition modifer applied to feature
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Modifier: " + mcmStr(annotation.modifier))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
Private Sub TotalRunoutData(annotation As DimXpertTolerance)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Total Runout Tolerance Compartment")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
Private Sub CircularRunoutData(annotation As DimXpertTolerance)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Circular Runout Tolerance Compartment")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
Private Sub LineProfileData(annotation As DimXpertLineProfileTolerance)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim I As Double, J As Double, K As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Line Profile Tolerance Compartment")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the outer (outside material) tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Outer Tolerance: " + FormatDouble(annotation.OuterToleranceValue))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the vector normal to the profile zones
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = annotation.GetPlanarZoneVector(I, J, K)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Planar Zone Vector: " + FormatVector(I, J, K))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
Private Sub CompositeLineProfileData(annotation As DimXpertCompositeLineProfileTolerance)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Composite Line Profile Tolerance Compartment")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the outer (outside material) tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Outer Tolerance: " + FormatDouble(annotation.OuterToleranceValue))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the vector normal to the profile zones
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = annotation.GetPlanarZoneVector(I, J, K)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Planar Zone Vector: " + FormatVector(I, J, K))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the datum reference frame for the orientation and form
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Composite Datums:")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Repeat Primary: " + IIf(annotation.PrimaryInLowerTier, "True", "False"))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Repeat Secondary: " + IIf(annotation.SecondaryInLowerTier, "True", "False"))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Repeat Tertiary: " + IIf(annotation.TertiaryInLowerTier, "True", "False"))
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}
End Sub
Private Sub SurfaceProfileData(annotation As DimXpertSurfaceProfileTolerance)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Surface Profile Tolerance Compartment")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the outer (outside material) tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Outer Tolerance: " + FormatDouble(annotation.OuterToleranceValue))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
Private Sub CompositeSurfaceProfileData(annotation As DimXpertCompositeSurfaceProfileTolerance)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Composite Surface Profile Tolerance Compartment")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance Upper Tier: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the outer tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Outer Tolerance Upper Tier: " + FormatDouble(annotation.OuterToleranceValue))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' the datum reference frame for the location
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the datum reference frame for the orientation and form
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Composite Datums:")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Repeat Primary: " + IIf(annotation.PrimaryInLowerTier, "True", "False"))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Repeat Secondary: " + IIf(annotation.SecondaryInLowerTier, "True", "False"))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Repeat Tertiary: " + IIf(annotation.TertiaryInLowerTier, "True", "False"))
End Sub
Private Sub OrientationData(annotation As DimXpertOrientationTolerance)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim I As Double, J As Double, K As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim enabled As Boolean, value As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim annoType As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}annoType = annotation.Type
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the type or orientation tolerance
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If annoType = swDimXpertGeoTol_Perpendicularity Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Orientation Type: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Perpendicularity")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertGeoTol_Parallelism Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Orientation Type: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Parallelism")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertGeoTol_Angularity Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Orientation Type: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Angularity")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Orientation Tolerance Compartment:")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the shape of the tolerance zone
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Select Case annotation.zoneType
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertOrientationZoneType_Cylindrical
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Zone Type: Cylindrical")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertOrientationZoneType_Planar
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Zone Type: Planar")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetPlanarZoneVector(I, J, K)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Planar Zone Vector: " + FormatVector(I, J, K))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'material condition modifer applied to feature
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Modifier: " + mcmStr(annotation.modifier))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the projected tolerance zone when specified
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = annotation.GetProjectedZone(enabled, value)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call FormatProjectedZone(enabled, value)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' is tangent plane
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}IsTangentPlane: " + IIf(annotation.IsTangentPlane, "True", "False"))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
Private Sub FlatnessData(annotation As DimXpertFlatnessTolerance)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim enabled As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim length As Double, width As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim I As Double, J As Double, K As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Flatness Tolerance Compartment:")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the per unit area data
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = annotation.GetPerUnitArea(enabled, length, width, I, J, K)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Per Unit Area: " + IIf(enabled, "True", "False"))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If enabled Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Per Unit Length: " + FormatDouble(length))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Per Unit Width: " + FormatDouble(width))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Per Unit Direction: " + FormatVector(I, J, K))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
Private Sub CircularityData(annotation As DimXpertTolerance)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Circularity Tolerance Compartment")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
Private Sub CylindricityData(annotation As DimXpertTolerance)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Cylindricity Tolerance Compartment")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
Private Sub StraightnessData(annotation As DimXpertStraightnessTolerance)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim I As Double, J As Double, K As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim enabled As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim dist As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}'tolerance compartment info
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Straightness Tolerance Compartment")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'type or shape of the tolerance zone
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Select Case annotation.zoneType
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertStraightnessZoneType_Cylindrical
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Zone Type: Cylindrical")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertStraightnessZoneType_PlanarMedian
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Zone Type: Planar Median")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertStraightnessZoneType_Surface
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Zone Type: Surface Straightness")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetPlanarZoneVector(I, J, K)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Zone Vector: " + FormatVector(I, J, K))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'per unit length
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = annotation.GetPerUnitLength(enabled, dist)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Per Unit Length: " + IIf(enabled, "True", "False"))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If enabled Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Per Unit Length Distance: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}" + FormatDouble(dist))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the material condition modifer
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Modifier: " + mcmStr(annotation.modifier))
End Sub
Private Sub ProfileData(annotation As DimXpertTolerance)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Profile Tolerance Compartment")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call DatumsStr(annotation)
End Sub
Private Sub SurfaceFinishData(annotation As DimXpertTolerance)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Surface Finish Tolerance Compartment")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
End Sub
Private Sub TangencyData(annotation As DimXpertTolerance)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Tangency Tolerance Compartment")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
End Sub
Private Sub DimensionToleranceData(annotation As DimXpertDimensionTolerance)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim isAngleType As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim annoType As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim upper As Double, lower As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim plus As Double, minus As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}annoType = annotation.Type
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}isAngleType = False
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Dimension Tolerance Compartment")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If annoType = swDimXpertDimTol_DistanceBetween Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim distancebetween As DimXpertDistanceBetweenDimTol
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set distancebetween = annotation
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call DistanceBetweenData(distancebetween)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertDimTol_CompositeDistanceBetween Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim compdistancebetween As DimXpertCompositeDistanceBetweenDimTol
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set compdistancebetween = annotation
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call CompositeDistanceBetweenData(compdistancebetween)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertDimTol_CounterBore Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim counterBore As IDimXpertCounterBoreDimTol
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set counterBore = annotation
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If counterBore.ReferenceFeature Is Nothing Then
kadov_tag{{<spaces>}}             kadov_tag{{</spaces>}}strs.Add ("Reference Feature: NULL")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add ("Reference Feature: " + counterBore.ReferenceFeature.Name)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertDimTol_Depth Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim depth As IDimXpertDepthDimTol
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set depth = annotation
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If depth.ReferenceFeature Is Nothing Then
kadov_tag{{<spaces>}}             kadov_tag{{</spaces>}}strs.Add ("Reference Feature: NULL")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add ("Reference Feature: " + depth.ReferenceFeature.Name)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertDimTol_CounterSinkDiameter Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim countersink As IDimXpertCounterSinkDiameterDimTol
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set countersink = annotation
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If countersink.ReferenceFeature Is Nothing Then
kadov_tag{{<spaces>}}             kadov_tag{{</spaces>}}strs.Add ("Reference Feature: NULL")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add ("Reference Feature: " + countersink.ReferenceFeature.Name)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertDimTol_ChamferDimension Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case annotation.ChamferType
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Case swDimXpertChamferDimensionType_Angle
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add ("Chamfer Dimension Type: Angle")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}isAngleType = True
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Case swDimXpertChamferDimensionType_LinearDistance1
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add ("Chamfer Dimension Type: Distance 1")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Case swDimXpertChamferDimensionType_LinearDistance2
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add ("Chamfer Dimension Type: Distance 2")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertDimTol_AngleBetween Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}isAngleType = True
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim angleBetween As IDimXpertAngleBetweenDimTol
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set angleBetween = annotation
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the origin and tolerance feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Origin Feature: " + angleBetween.OriginFeature.Name)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' is supplement angle
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Supplement Angle: " + IIf(angleBetween.Supplement, "True", "False"))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertDimTol_CounterSinkAngle Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}isAngleType = True
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim countersinkAngle As IDimXpertCounterSinkAngleDimTol
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set countersinkAngle = annotation
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If countersinkAngle.ReferenceFeature Is Nothing Then
kadov_tag{{<spaces>}}             kadov_tag{{</spaces>}}strs.Add ("Reference Feature: NULL")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add ("Reference Feature: " + countersinkAngle.ReferenceFeature.Name)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertDimTol_ConeAngle Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}isAngleType = True
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' conversion for radians to degrees when dimension type is angle
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim dbl As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If isAngleType Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}dbl = 57.2957795130823
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}dbl = 1#
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the nominal, and upper and lower limits of size of the dimension
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Compute Nominal Dimension: " + FormatDouble(annotation.GetNominalValue * dbl))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = annotation.GetUpperAndLowerLimit(upper, lower)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Get Upper Limit: " + FormatDouble(upper * dbl))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Get Lower Limit: " + FormatDouble(lower * dbl))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the upper and lower tolerance value by type
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Select Case annotation.DimensionType
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTolType_BlockTolerance
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Dimension Type: Block Tolerance")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' block tolerance
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTolType_BlockToleranceNoNominal
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim blockTols As DimXpertBlockTolerances
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set blockTols = dimXpertPart.GetBlockTolerances
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case blockTols.Type
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertBlockToleranceType_ASMEInch
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add ("Dimension Type: Block Tolerance No Nominal")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}If isAngleType Then
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}strs.Add ("Angular Block Tolerance")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}strs.Add ("Block Tolerance Decimal Places: " + Format(annotation.BlockToleranceDecimalPlaces, "##,##0"))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertBlockToleranceType_ISO2768
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add ("Dimension Type: General Tolerance")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTolType_ISOLimitsAndFits
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Dimension Type: Limits and Fits")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' limits and fits tolerance
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTolType_ISOLimitsAndFitsNoNominal
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Dimension Type: Limits and Fits No Nominal")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Limits and Fits: " + annotation.LimitsAndFitsCode)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' limit dimension
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTolType_LimitDimension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Dimension Type: Limit Dimension")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetUpperAndLowerLimit(upper, lower)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Get Upper Limit: " + FormatDouble(upper * dbl))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Get Lower Limit: " + FormatDouble(lower * dbl))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTolType_MAXTolerance
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Dimension Type: MAXTolerance")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTolType_MINTolerance
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Dimension Type: MINTolerance")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTolType_NoTolerance
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Dimension Type: NoTolerance")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTolType_PlusMinusDimension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Dimension Type: Plus Minus Dimension")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' plus and minus dimension
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTolType_PlusMinusNoNominal
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Dimension Type: Plus Minus No Nominal")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetPlusAndMinusTolerance(plus, minus)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Plus kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(plus * dbl))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Minus Tolerance: " + FormatDouble(minus * dbl))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
End Sub
Private Sub DistanceBetweenData(annotation As DimXpertDistanceBetweenDimTol)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim feature As DimXpertFeature
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim featureFosUsage As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim I As Double, J As Double, K As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the origin and tolerance feature along with their feature of size usage (min, max, center)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = annotation.GetOriginFeature(feature, featureFosUsage)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Origin Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = annotation.GetFeature(feature, featureFosUsage)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Tolerance Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' The direction vector
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = annotation.GetDirectionVector(I, J, K)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Direction Vector: " + FormatVector(I, J, K))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
End Sub
Private Sub CompositeDistanceBetweenData(annotation As DimXpertCompositeDistanceBetweenDimTol)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim feature As DimXpertFeature
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim featureFosUsage As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim plus As Double, minus As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim I As Double, J As Double, K As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim blockTols As DimXpertBlockTolerances
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the origin and tolerance feature along with their feature of size usage (min, max, center)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = annotation.GetOriginFeature(feature, featureFosUsage)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Origin Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = annotation.GetFeature(feature, featureFosUsage)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Tolerance Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the pattern locating feature
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = annotation.GetIntraFeature(feature, featureFosUsage)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Pattern Locating Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' The direction vector
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = annotation.GetDirectionVector(I, J, K)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Direction Vector: " + FormatVector(I, J, K))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the upper and lower tolerance value for the pattern location by type
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Select Case annotation.DimensionType
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' plus and minus dimension
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTolType_PlusMinusNoNominal
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Pattern Locating Dimension Type: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Plus Minus No Nominal")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetPlusAndMinusToleranceIntraFeature(plus, minus)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Plus kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(plus))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Minus Tolerance: " + FormatDouble(minus))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' block tolerance
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTolType_BlockToleranceNoNominal
kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set blockTols = dimXpertPart.GetBlockTolerances
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case blockTols.Type
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Case swDimXpertBlockToleranceType_ASMEInch
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add ("Pattern Locating Dimension Type: Block Tolerance No Nominal")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Block Tolerance Decimal Places: " + Format(annotation.BlockToleranceDecimalPlaces, "##,##0"))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Case swDimXpertBlockToleranceType_ISO2768
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add ("Pattern Locating Dimension Type: General Tolerance")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' the upper and lower tolerance value for the feature to feature location by type
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Select Case annotation.DimensionTypeIntraFeature
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' plus and minus dimension
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTolType_PlusMinusNoNominal
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add ("Feature Locating Dimension Type: Plus Minus No Nominal")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetPlusAndMinusToleranceIntraFeature(plus, minus)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Plus kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(plus))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Minus Tolerance: " + FormatDouble(minus))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' block tolerance
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTolType_BlockToleranceNoNominal
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set blockTols = dimXpertPart.GetBlockTolerances
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case blockTols.Type
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Case swDimXpertBlockToleranceType_ASMEInch
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add ("Feature locating Dimension Type: Block Tolerance No Nominal")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Block Tolerance Decimal Places: " + Format(annotation.BlockToleranceDecimalPlacesIntraFeature, "##,##0"))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Case swDimXpertBlockToleranceType_ISO2768
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add ("Feature locating Dimension Type: General Tolerance")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
Private Sub DatumsStr(annotation As DimXpertTolerance)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strs.Add ("Datums:")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call datumStr(annotation.GetPrimaryDatums(), annotation.GetPrimaryDatumModifiers(), " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Primary:")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call datumStr(annotation.GetSecondaryDatums(), annotation.GetSecondaryDatumModifiers(), " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Secondary:")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call datumStr(annotation.GetTertiaryDatums(), annotation.GetTertiaryDatumModifiers(), " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tertiary:")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
Private Sub datumStr(dats As Variant, mods As Variant, datumOrder As String)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim I kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim str As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim mcm As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If IsEmpty(dats) Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (datumOrder + ": none")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}For I = LBound(dats) To UBound(dats)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}mcm = mods(I)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = str + " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}" + dats(I).Identifier + " @ " + mcmStr(mcm)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Next I
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If StrComp(str, "") > 0 Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (datumOrder + str)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (datumOrder + " <none>")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
End Sub
' returns a string containing the height of the projected tolerance zone
Private Sub FormatProjectedZone(enabled As Boolean, height As Double)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If enabled = True Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Projected Zone: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}True")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Zone Height: " + FormatDouble(height))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Projected Zone: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}False")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
Private Function mcmStr(mcm As Long) As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim str
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Select Case mcm
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertMCM_LMC
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "LMC"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertMCM_MMC
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "MMC"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertMCM_NoMCM
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "NoMCM"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertMCM_RFS
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "RFS"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}mcmStr = str
End Function
' returns a string containing the type of position tolerance zone used
Private Function PositionZoneType(typ As Long) As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim str As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Select Case typ
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertPositionZoneType_CylindricalPosition
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "Cylindrical"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertPositionZoneType_PlanarPosition
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "Planar"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertPositionZoneType_SphericalPosition
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "Spherical"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertPositionZoneType_Boundary
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "Boundary"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertPositionZoneType_RadialPositionArc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "RadialPositionArc"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertPositionZoneType_RadialPositionPlanar
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "RadialPositionPlanar"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case Else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "N/A"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}PositionZoneType = str
End Function
' returns a string containing the names of the SW display entities
Private Function DisplayEntity(annotation As DimXpertAnnotation) As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim str As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim dispEnt As Object
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swAnnot As SldWorks.annotation
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Set dispEnt = swDimXpert.GetDisplayEntity(annot)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set dispEnt = annotation.GetDisplayEntity
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If Not dispEnt Is Nothing Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If TypeOf dispEnt Is SldWorks.annotation Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set swAnnot = dispEnt
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}str = swAnnot.GetName
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}DisplayEntity = str
End Function
' returns a string containing the feature of size usage (min, max, center)
Private Function FosUsage(value As Long) As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim str
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Select Case value
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDistanceFosUsage_Center
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "Center"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDistanceFosUsage_MaximumSide
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "Max"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDistanceFosUsage_MinimumSide
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "Min"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case Else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "N/A"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}FosUsage = str
End Function
Private Function FormatVector(I As Double, J As Double, K As Double) As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim str
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}str = FormatDouble(I) + ", " + FormatDouble(J) + ", " + FormatDouble(K)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}FormatVector = str
End Function
Private Function FormatDouble(value As Double) As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim str
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}str = Format(value, "##,##0.0000")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}FormatDouble = str
End Function
Private Function RadiansToDegrees(value As Double) As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim str
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}str = Format((value * 57.2957795130823), "##,##0.00")
kadov_tag{{<spaces>}}                  kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}RadiansToDegrees = str
End Function
Private Function annotationTypeNameFromObject(anno As DimXpertAnnotation) As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}annotationTypeNameFromObject = annotationTypeNameFromTypeNumber(anno.Type)
End Function
Private Function annotationTypeNameFromTypeNumber(annoTypeIndex As Long) As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Select Case annoTypeIndex
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTol_DistanceBetween
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "DistanceBetween Dim"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTol_CounterBore
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "CounterBore Dim"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTol_Depth
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Depth Dim"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTol_CounterSinkDiameter
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "CounterSinkDiameter Dim"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTol_ChamferDimension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "ChamferDimension Dim"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTol_AngleBetween
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "AngleBetween Dim"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTol_CounterSinkAngle
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "CounterSinkAngle Dim"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTol_ConeAngle
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "ConeAngle Dim"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTol_Diameter
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Diameter Dim"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTol_Length
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Length Dim"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTol_Radius
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Radius Dim"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTol_Width
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Width Dim"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDimTol_CompositeDistanceBetween
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "CompositeDistanceBetween Dim"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertDatum
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Datum"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertGeoTol_Position
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Position Tol"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertGeoTol_CompositePosition
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "CompositePosition Tol"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertGeoTol_Symmetry
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Symmetry Tol"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertGeoTol_Concentricity
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Concentricity Tol"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertGeoTol_LineProfile
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "LineProfile Tol"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertGeoTol_CompositeLineProfile
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "CompositeLineProfile Tol"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertGeoTol_SurfaceProfile
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "SurfaceProfile Tol"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertGeoTol_CompositeSurfaceProfile
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "CompositeSurfaceProfile Tol"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertGeoTol_Angularity
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Angularity Tol"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertGeoTol_Parallelism
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Parallelism Tol"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertGeoTol_Perpendicularity
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Perpendicularity Tol"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertGeoTol_TotalRunout
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "TotalRunout Tol"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertGeoTol_CircularRunout
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "CircularRunout Tol"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertGeoTol_Flatness
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Flatness Tol"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertGeoTol_Circularity
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Circularity Tol"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertGeoTol_Cylindricity
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Cylindricity Tol"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertGeoTol_Straightness
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Straightness Tol"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swDimXpertGeoTol_Tangency
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Tangency Tol"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case Else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "<unknown> " & CStr(annoTypeIndex)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Select
End Function
```
