---
title: "Get DimXpert Datum Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Datum_Example_VBNET.htm"
---

# Get DimXpert Datum Example (VB.NET)

This example shows how to build a part and get attributes for the DimXpert
Datum annotation.

```vb
'----------------------------------------------------------------------------
' Preconditions:
'  kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1. Open public_documents\samples\tutorial\cosmosfloxpress\ball valve\ball.sldprt.
'  kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2. Open the DimXpert toolbar from View > Toolbars.
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}} 3. Click the Add DimXpert datum icon on the DimXpert toolbar.
' kadov_tag{{<spaces>}} 4. Click the ball of the part.
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}} 5. Click to place the datum annotation.
' kadov_tag{{<spaces>}} 6. Click the green check mark to accept the new datum feature.
' kadov_tag{{<spaces>}} 7. Observe the following DimXpert features on the DimXpertManager tab
'     of the Management Panel:kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Sphere1.
' kadov_tag{{<spaces>}} 8. Open an Immediate window.
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}} 9. Ensure that the SolidWorks.Interop.swdimxpert.dll interop assembly
'     is loaded (right-click project in Project Explorer and
'     click Add Reference > .NET tab).
' kadov_tag{{<spaces>}}10. Ensure that the Microsoft Scripting Runtime library is loaded
' kadov_tag{{<spaces>}}    (right-click project in Project Explorer and  click Add Reference >
'     COM tab).
'
' Postconditions:
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}} 1. Writes the output of this macro to c:\temp\dimXpertInfo.txt.
'  kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2. Inspect the Immediate Window.
'
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}NOTE: Because this part is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swdimxpert
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Imports Scripting
Partial Class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim strs As New Collection
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim dimXpertPart As DimXpertPart
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim i As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim j As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim k As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDoc As IModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDoc = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If swModelDoc Is Nothing Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim fso As New Scripting.FileSystemObject()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim f As Scripting.File
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim textStr As Scripting.TextStream
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}textStr = fso.CreateTextFile("c:\temp\dimXpertInfo.txt")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}f = fso.GetFile("c:\temp\dimXpertInfo.txt")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'textStr = f.OpenAsTextStream(2, -2)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If textStr Is Nothing Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Error creating temp file.")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call log("Starting DimXpert log...", textStr)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call retrieve_info_text(swApp, textStr)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}textStr.Close()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub log(ByVal text As String, ByVal textStr As Scripting.TextStream)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(text)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}textStr.WriteLine(text)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub retrieve_info_text(ByVal swapp As SldWorks, ByVal textStr As TextStream)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim dimXpertMgr As SolidWorks.Interop.sldworks.DimXpertManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}dimXpertMgr = swapp.IActiveDoc2.Extension.DimXpertManager(swapp.IActiveDoc2.IGetActiveConfiguration().Name, True)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call log("Model: " & swapp.IActiveDoc2.GetPathName, textStr)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim dimXpertPartObj As DimXpertPart
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}dimXpertPartObj = dimXpertMgr.DimXpertPart
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}dimXpertPart = dimXpertPartObj
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim vAnnotations As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}vAnnotations = dimXpertPart.GetAnnotations()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call log("------------------------", textStr)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call log("Annotations...", textStr)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call log("------------------------", textStr)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim annotationTemp As DimXpertAnnotation
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim annotationIndex As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For annotationIndex = 0 To UBound(vAnnotations)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}annotationTemp = vAnnotations(annotationIndex)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim AnnotationDataText As Collection
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AnnotationDataText = AnnotationData(annotationTemp)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim annotationTextIndex As Long
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}For annotationTextIndex = 1 To AnnotationDataText.Count
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Call log(AnnotationDataText(annotationTextIndex), textStr)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Next
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Function AnnotationData(ByVal annotation As DimXpertAnnotation) As Collection
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim annoType As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'general info
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call GeneralInfo(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annoType = annotation.Type
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If annoType = swDimXpertAnnotationType_e.swDimXpertDatum Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call DatumData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Position Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call PositionData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositePosition Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call CompositePositionData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Symmetry Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call SymmetryData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Concentricity Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call ConcentricityData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_LineProfile Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call LineProfileData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeLineProfile Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call CompositeLineProfileData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_SurfaceProfile Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call SurfaceProfileData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeSurfaceProfile Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call CompositeSurfaceProfileData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Angularity Or annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Parallelism Or annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Perpendicularity Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call OrientationData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_TotalRunout Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call TotalRunoutData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_CircularRunout Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call CircularRunoutData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Flatness Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call FlatnessData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Circularity Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call CircularityData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Cylindricity Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call CylindricityData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Straightness Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call StraightnessData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Tangency Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call TangencyData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' any of the dimension tolerance types
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call DimensionToleranceData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AnnotationData = strs
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub Clear(ByVal strs As Collection)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Remove(strs.Count)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Not strs.Count = 0 Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call Clear(strs)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub GeneralInfo(ByVal annotation As DimXpertAnnotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim annoType As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim modelObj As Feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Not strs.Count = 0 Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call Clear(strs)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Name: " + annotation.Name)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annoType = annotationTypeNameFromObject(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Type: " + annoType)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Display Entity: " + DisplayEntity(annotation))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}modelObj = annotation.GetModelFeature()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Not (modelObj Is Nothing) Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("ModelFeature: " + modelObj.Name + " (" + modelObj.GetTypeName2() + ")")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub DatumData(ByVal annotation As DimXpertDatum)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the datum letter
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Datum Letter: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}" + annotation.Identifier)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub PositionData(ByVal annotation As DimXpertPositionTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim I As Double, J As Double, K As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim enabled As Boolean, value As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Position Tolerance Compartment:")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the shape of the tolerance zone
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Zone Type: " + PositionZoneType(annotation.ZoneType))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the zone vector if the tolerance zone is planar
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If annotation.ZoneType = swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_PlanarPosition Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = annotation.GetPlanarZoneVector(I, J, K)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Direction: " + FormatVector(I, J, K))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the material condition modifier applied to feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Modifier: " + mcmStr(annotation.Modifier))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the projected tolerance zone when specified
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetProjectedZone(enabled, value)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call FormatProjectedZone(enabled, value)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub CompositePositionData(ByVal annotation As DimXpertCompositePositionTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim I As Double, J As Double, K As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim enabled As Boolean, value As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Composite Position Tolerance Compartment")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the shape of the tolerance zone
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Zone Type: " + PositionZoneType(annotation.ZoneType))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the zone vector when the zone is planar
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If annotation.ZoneType = swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_PlanarPosition Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = annotation.GetPlanarZoneVector(I, J, K)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Direction: " + FormatVector(I, J, K))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the material condition modifier
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Modifier: " + mcmStr(annotation.Modifier))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the projected tolerance zone when specified
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetProjectedZone(enabled, value)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call FormatProjectedZone(enabled, value)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the datum reference frame for the pattern location
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the datum reference frame for the feature to feature location
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Composite datums:")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Repeat Primary: " + IIf(annotation.PrimaryInLowerTier, "True", "False"))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Repeat Secondary: " + IIf(annotation.SecondaryInLowerTier, "True", "False"))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Repeat Tertiary: " + IIf(annotation.TertiaryInLowerTier, "True", "False"))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub SymmetryData(ByVal annotation As DimXpertSymmetryTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim I As Double, J As Double, K As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Symmetry Tolerance Compartment")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the material condition modifier applied to feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Modifier: " + mcmStr(annotation.Modifier))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the direction of the planar zone
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetZoneDirection(I, J, K)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Planar Zone Direction: " + FormatVector(I, J, K))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub ConcentricityData(ByVal annotation As DimXpertConcentricityTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Concentricity Tolerance Compartment")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the material condition modifier applied to feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Modifier: " + mcmStr(annotation.Modifier))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub TotalRunoutData(ByVal annotation As DimXpertTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Total Runout Tolerance Compartment")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub CircularRunoutData(ByVal annotation As DimXpertTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Ciircular Runout Tolerance Compartment")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub LineProfileData(ByVal annotation As DimXpertLineProfileTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim I As Double, J As Double, K As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Line Profile Tolerance Compartment")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the outer (outside material) tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Outer Tolerance: " + FormatDouble(annotation.OuterToleranceValue))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the vector normal to the profile zones
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetPlanarZoneVector(I, J, K)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Planar Zone Vector: " + FormatVector(I, J, K))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub CompositeLineProfileData(ByVal annotation As DimXpertCompositeLineProfileTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Composite Line Profile Tolerance Compartment")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the outer (outside material) tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Outer Tolerance: " + FormatDouble(annotation.OuterToleranceValue))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the vector normal to the profile zones
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetPlanarZoneVector(i, j, k)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Planar Zone Vector: " + FormatVector(i, j, k))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the datum reference frame for the orientation and form
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Composite Datums:")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Repeat Primary: " + IIf(annotation.PrimaryInLowerTier, "True", "False"))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Repeat Secondary: " + IIf(annotation.SecondaryInLowerTier, "True", "False"))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Repeat Tertiary: " + IIf(annotation.TertiaryInLowerTier, "True", "False"))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub SurfaceProfileData(ByVal annotation As DimXpertSurfaceProfileTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Surface Profile Tolerance Compartment")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the outer (outside material) tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Outer Tolerance: " + FormatDouble(annotation.OuterToleranceValue))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub CompositeSurfaceProfileData(ByVal annotation As DimXpertCompositeSurfaceProfileTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Composite Surface Profile Tolerance Compartment")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance Upper Tier: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the outer tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Outer Tolerance Upper Tier: " + FormatDouble(annotation.OuterToleranceValue))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the datum reference frame for the location
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the datum reference frame for the orientation and form
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Composite Datums:")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Repeat Primary: " + IIf(annotation.PrimaryInLowerTier, "True", "False"))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Repeat Secondary: " + IIf(annotation.SecondaryInLowerTier, "True", "False"))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Repeat Tertiary: " + IIf(annotation.TertiaryInLowerTier, "True", "False"))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub OrientationData(ByVal annotation As DimXpertOrientationTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim I As Double, J As Double, K As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim enabled As Boolean, value As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim annoType As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annoType = annotation.Type
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the type or orientation tolerance
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Perpendicularity Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Orientation Type: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Perpendicularity")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Parallelism Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Orientation Type: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Parallelism")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Angularity Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Orientation Type: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Angularity")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Orientation Tolerance Compartment:")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the shape of the tolerance zone
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case annotation.ZoneType
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertOrientationZoneType_e.swDimXpertOrientationZoneType_Cylindrical
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Zone Type: Cylindrical")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertOrientationZoneType_e.swDimXpertOrientationZoneType_Planar
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Zone Type: Planar")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}boolstatus = annotation.GetPlanarZoneVector(I, J, K)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Planar Zone Vector: " + FormatVector(I, J, K))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'material condition modifier applied to feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Modifier: " + mcmStr(annotation.Modifier))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the projected tolerance zone when specified
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetProjectedZone(enabled, value)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call FormatProjectedZone(enabled, value)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' is tangent plane
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}IsTangentPlane: " + IIf(annotation.IsTangentPlane, "True", "False"))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub FlatnessData(ByVal annotation As DimXpertFlatnessTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim enabled As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim length As Double, width As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim I As Double, J As Double, K As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Flatness Tolerance Compartment:")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the per unit area data
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetPerUnitArea(enabled, length, width, I, J, K)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Per Unit Area: " + IIf(enabled, "True", "False"))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If enabled Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Per Unit Length: " + FormatDouble(length))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Per Unit Width: " + FormatDouble(width))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Per Unit Direction: " + FormatVector(I, J, K))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub CircularityData(ByVal annotation As DimXpertTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Circularity Tolerance Compartment")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub CylindricityData(ByVal annotation As DimXpertTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Cylindricity Tolerance Compartment")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub StraightnessData(ByVal annotation As DimXpertStraightnessTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim I As Double, J As Double, K As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim enabled As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim dist As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'tolerance compartment info
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Straightness Tolerance Compartment")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'type or shape of the tolerance zone
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case annotation.ZoneType
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertStraightnessZoneType_e.swDimXpertStraightnessZoneType_Cylindrical
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Zone Type: Cylindrical")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertStraightnessZoneType_e.swDimXpertStraightnessZoneType_PlanarMedian
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Zone Type: Planar Median")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertStraightnessZoneType_e.swDimXpertStraightnessZoneType_Surface
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Zone Type: Surface Straightness")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}boolstatus = annotation.GetPlanarZoneVector(I, J, K)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Zone Vector: " + FormatVector(I, J, K))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'per unit length
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetPerUnitLength(enabled, dist)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Per Unit Length: " + IIf(enabled, "True", "False"))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If enabled Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Per Unit Length Distance: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}" + FormatDouble(dist))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the material condition modifier
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Modifier: " + mcmStr(annotation.Modifier))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub ProfileData(ByVal annotation As DimXpertTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Profile Tolerance Compartment")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call DatumsStr(annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub SurfaceFinishData(ByVal annotation As DimXpertTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Surface Finish Tolerance Compartment")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub TangencyData(ByVal annotation As DimXpertTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tangency Tolerance Compartment")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(annotation.Tolerance))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub DimensionToleranceData(ByVal annotation As DimXpertDimensionTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim isAngleType As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim annoType As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim upper As Double, lower As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim plus As Double, minus As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annoType = annotation.Type
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}isAngleType = False
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Dimension Tolerance Compartment")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_DistanceBetween Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call DistanceBetweenData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_CompositeDistanceBetween Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call CompositeDistanceBetweenData(annotation)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_CounterBore Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If annotation.ReferenceFeature Is Nothing Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Reference Feature: NULL")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Reference Feature: " + annotation.ReferenceFeature.Name)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_Depth Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If annotation.ReferenceFeature Is Nothing Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Reference Feature: NULL")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Reference Feature: " + annotation.ReferenceFeature.Name)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkDiameter Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If annotation.ReferenceFeature Is Nothing Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Reference Feature: NULL")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Reference Feature: " + annotation.ReferenceFeature.Name)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_ChamferDimension Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim chamferAnno As IDimXpertChamferDimTol
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}chamferAnno = annotation
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Select Case chamferAnno.ChamferType
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Case swDimXpertChamferDimensionType_e.swDimXpertChamferDimensionType_Angle
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}strs.Add("Chamfer Dimension Type: Angle")
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}isAngleType = True
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Case swDimXpertChamferDimensionType_e.swDimXpertChamferDimensionType_LinearDistance1
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}strs.Add("Chamfer Dimension Type: Distance 1")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Case swDimXpertChamferDimensionType_e.swDimXpertChamferDimensionType_LinearDistance2
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}strs.Add("Chamfer Dimension Type: Distance 2")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_AngleBetween Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}isAngleType = True
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' the origin and tolerance feature
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Origin Feature: " + annotation.OriginFeature.Name)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' is supplement angle
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Supplement Angle: " + IIf(annotation.Supplement, "True", "False"))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkAngle Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}isAngleType = True
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If annotation.ReferenceFeature Is Nothing Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Reference Feature: NULL")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Reference Feature: " + annotation.ReferenceFeature.Name)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_ConeAngle Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}isAngleType = True
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' conversion for radians to degrees when dimension type is angle
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim dbl As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If isAngleType Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dbl = 57.2957795130823
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dbl = 1.0#
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the nominal, and upper and lower limits of size of the dimension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Compute Nominal Dimension: " + FormatDouble(annotation.GetNominalValue * dbl))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetUpperAndLowerLimit(upper, lower)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Get Upper Limit: " + FormatDouble(upper * dbl))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Get Lower Limit: " + FormatDouble(lower * dbl))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the upper and lower tolerance value by type
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case annotation.DimensionType
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockTolerance
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Dimension Type: Block Tolerance")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}' block tolerance
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockToleranceNoNominal
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Dim blockTols As DimXpertBlockTolerances
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}blockTols = dimXpertPart.GetBlockTolerances
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Select Case blockTols.Type
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ASMEInch
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}strs.Add("Dimension Type: Block Tolerance No Nominal")
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}If isAngleType Then
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}strs.Add("Angular Block Tolerance")
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}strs.Add("Block Tolerance Decimal Places: " + Format(annotation.BlockToleranceDecimalPlaces, "##,##0"))
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ISO2768
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}strs.Add("Dimension Type: General Tolerance")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_ISOLimitsAndFits
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Dimension Type: Limits and Fits")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}' limits and fits tolerance
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_ISOLimitsAndFitsNoNominal
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Dimension Type: Limits and Fits No Nominal")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Limits and Fits: " + annotation.LimitsAndFitsCode)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}' limit dimension
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_LimitDimension
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Dimension Type: Limit Dimension")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}boolstatus = annotation.GetUpperAndLowerLimit(upper, lower)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Get Upper Limit: " + FormatDouble(upper * dbl))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Get Lower Limit: " + FormatDouble(lower * dbl))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_MAXTolerance
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Dimension Type: MAXTolerance")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_MINTolerance
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Dimension Type: MINTolerance")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_NoTolerance
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Dimension Type: NoTolerance")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusDimension
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Dimension Type: Plus Minus Dimension")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}' plus and minus dimension
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusNoNominal
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Dimension Type: Plus Minus No Nominal")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}boolstatus = annotation.GetPlusAndMinusTolerance(plus, minus)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Plus kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(plus * dbl))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Minus Tolerance: " + FormatDouble(minus * dbl))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub DistanceBetweenData(ByVal annotation As DimXpertDistanceBetweenDimTol)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim feature As DimXpertFeature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim featureFosUsage As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim I As Double, J As Double, K As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}feature = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the origin and tolerance feature along with their feature of size usage (min, max, center)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetOriginFeature(feature, featureFosUsage)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Origin Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetFeature(feature, featureFosUsage)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' The direction vector
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetDirectionVector(I, J, K)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Direction Vector: " + FormatVector(I, J, K))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub CompositeDistanceBetweenData(ByVal annotation As DimXpertCompositeDistanceBetweenDimTol)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim feature As DimXpertFeature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim featureFosUsage As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim plus As Double, minus As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim I As Double, J As Double, K As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}feature = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the origin and tolerance feature along with their feature of size usage (min, max, center)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetOriginFeature(feature, featureFosUsage)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Origin Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetFeature(feature, featureFosUsage)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the pattern locating feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetIntraFeature(feature, featureFosUsage)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Pattern Locating Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' The direction vector
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetDirectionVector(I, J, K)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Direction Vector: " + FormatVector(I, J, K))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the upper and lower tolerance value for the pattern location by type
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim dimTol As IDimXpertDimensionTolerance
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}dimTol = annotation
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case dimTol.DimensionType
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' plus and minus dimension
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusNoNominal
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}dimTol.GetPlusAndMinusTolerance(plus, minus)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Pattern Locating Dimension Type: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Plus Minus No Nominal")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Plus kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(plus))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Minus Tolerance: " + FormatDouble(minus))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}' block tolerance
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockToleranceNoNominal
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Dim blockTols As DimXpertBlockTolerances
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}blockTols = dimXpertPart.GetBlockTolerances
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Select Case blockTols.Type
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ASMEInch
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}strs.Add("Pattern Locating Dimension Type: Block Tolerance No Nominal")
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Block Tolerance Decimal Places: " + Format(annotation.BlockToleranceDecimalPlaces, "##,##0"))
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ISO2768
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}strs.Add("Pattern Locating Dimension Type: General Tolerance")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the upper and lower tolerance value for the feature to feature location by type
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case annotation.DimensionTypeIntraFeature
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' plus and minus dimension
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusNoNominal
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Feature Locating Dimension Type: Plus Minus No Nominal")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}boolstatus = annotation.GetPlusAndMinusToleranceIntraFeature(plus, minus)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Plus kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance: " + FormatDouble(plus))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Minus Tolerance: " + FormatDouble(minus))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}' block tolerance
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockToleranceNoNominal
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Dim blockTols As DimXpertBlockTolerances
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}blockTols = dimXpertPart.GetBlockTolerances
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Select Case blockTols.Type
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ASMEInch
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}strs.Add("Feature locating Dimension Type: Block Tolerance No Nominal")
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Block Tolerance Decimal Places: " + Format(annotation.BlockToleranceDecimalPlacesIntraFeature, "##,##0"))
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ISO2768
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}strs.Add("Feature locating Dimension Type: General Tolerance")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub DatumsStr(ByVal annotation As DimXpertTolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Datums:")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call datumStr(annotation.GetPrimaryDatums(), annotation.GetPrimaryDatumModifiers(), " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Primary:")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call datumStr(annotation.GetSecondaryDatums(), annotation.GetSecondaryDatumModifiers(), " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Secondary:")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call datumStr(annotation.GetTertiaryDatums(), annotation.GetTertiaryDatumModifiers(), " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tertiary:")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub datumStr(ByVal dats As Object, ByVal mods As Object, ByVal datumOrder As String)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim I As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim str As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim mcm As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If IsNothing(dats) Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = ""
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For I = LBound(dats) To UBound(dats)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}mcm = mods(I)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}str = str + " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}" + dats(I).Identifier + " @ " + mcmStr(mcm)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next I
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If StrComp(str, "") > 0 Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(datumOrder + str)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(datumOrder + " <none>")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' returns a string containing the heith of the projected tolerance zone
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub FormatProjectedZone(ByVal enabled As Boolean, ByVal height As Double)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If enabled = True Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Projected Zone: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}True")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Zone Height: " + FormatDouble(height))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Projected Zone: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}False")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function mcmStr(ByVal mcm As Long) As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim str As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = ""
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case mcm
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertMaterialConditionModifier_e.swDimXpertMCM_LMC
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "LMC"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertMaterialConditionModifier_e.swDimXpertMCM_MMC
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "MMC"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertMaterialConditionModifier_e.swDimXpertMCM_NoMCM
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "NoMCM"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertMaterialConditionModifier_e.swDimXpertMCM_RFS
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "RFS"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}mcmStr = str
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' returns a string containing the type of position tolerance zone used
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function PositionZoneType(ByVal typ As Long) As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim str As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case typ
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_CylindricalPosition
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "Cylindrical"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_PlanarPosition
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "Planar"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_SphericalPosition
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "Spherical"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_Boundary
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "Boundary"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_RadialPositionArc
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "RadialPositionArc"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_RadialPositionPlanar
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "RadialPositionPlanar"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case Else
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "N/A"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}PositionZoneType = str
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' returns a string containing the names of the SW display entities
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function DisplayEntity(ByVal annotation As DimXpertAnnotation) As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim str As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim dispEnt As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swAnnot As SolidWorks.Interop.sldworks.Annotation
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = ""
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Set dispEnt = swDimXpert.GetDisplayEntity(annot)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}dispEnt = annotation.GetDisplayEntity()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Not dispEnt Is Nothing Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If TypeOf dispEnt Is SolidWorks.Interop.sldworks.Annotation Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swAnnot = dispEnt
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = swAnnot.GetName
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DisplayEntity = str
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' returns a string containing the feature of size usage (min, max, center)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function FosUsage(ByVal value As Long) As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim str As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case value
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertDistanceFosUsage_e.swDimXpertDistanceFosUsage_Center
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "Center"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertDistanceFosUsage_e.swDimXpertDistanceFosUsage_MaximumSide
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "Max"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertDistanceFosUsage_e.swDimXpertDistanceFosUsage_MinimumSide
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "Min"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case Else
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "N/A"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}FosUsage = str
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function FormatVector(ByVal I As Double, ByVal J As Double, ByVal K As Double) As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim str As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = FormatDouble(I) + ", " + FormatDouble(J) + ", " + FormatDouble(K)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}FormatVector = str
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function FormatDouble(ByVal value As Double) As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim str As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = Format(value, "##,##0.0000")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}FormatDouble = str
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function RadiansToDegrees(ByVal value As Double) As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim str As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = Format((value * 57.2957795130823), "##,##0.00")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}RadiansToDegrees = str
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function annotationTypeNameFromObject(ByVal anno As DimXpertAnnotation) As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annotationTypeNameFromObject = annotationTypeNameFromTypeNumber(anno.Type)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function annotationTypeNameFromTypeNumber(ByVal annoTypeIndex As Long) As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case annoTypeIndex
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertDimTol_DistanceBetween
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "DistanceBetween Dim"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertDimTol_CounterBore
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "CounterBore Dim"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertDimTol_Depth
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Depth Dim"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkDiameter
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "CounterSinkDiameter Dim"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertDimTol_ChamferDimension
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "ChamferDimension Dim"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertDimTol_AngleBetween
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "AngleBetween Dim"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkAngle
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "CounterSinkAngle Dim"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertDimTol_ConeAngle
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "ConeAngle Dim"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertDimTol_Diameter
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Diameter Dim"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertDimTol_Length
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Length Dim"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertDimTol_Radius
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Radius Dim"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertDimTol_Width
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Width Dim"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertDimTol_CompositeDistanceBetween
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "CompositeDistanceBetween Dim"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertDatum
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Datum"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Position
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Position Tol"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositePosition
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "CompositePosition Tol"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Symmetry
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Symmetry Tol"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Concentricity
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Concentricity Tol"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertGeoTol_LineProfile
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "LineProfile Tol"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeLineProfile
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "CompositeLineProfile Tol"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertGeoTol_SurfaceProfile
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "SurfaceProfile Tol"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeSurfaceProfile
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "CompositeSurfaceProfile Tol"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Angularity
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Angularity Tol"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Parallelism
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Parallelism Tol"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Perpendicularity
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Perpendicularity Tol"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertGeoTol_TotalRunout
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "TotalRunout Tol"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertGeoTol_CircularRunout
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "CircularRunout Tol"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Flatness
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Flatness Tol"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Circularity
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Circularity Tol"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Cylindricity
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Cylindricity Tol"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Straightness
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Straightness Tol"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Tangency
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "Tangency Tol"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case Else
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTypeNameFromTypeNumber = "<unknown> " & CStr(annoTypeIndex)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks
End Class
```
