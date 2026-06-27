---
title: "Get and Set Location Dimension Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_and_Set_Location_Dimension_Example_VB.htm"
---

# Get and Set Location Dimension Example (VBA)

This example shows how to get and set DimXpert distance-between or angle-between dimensions.

```vb
 '---------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\dimxpert\bracket_ads_plusminus.sldprt.
 ' 2. Multi-select two faces that:
 '    a. share a common edge to get the angle-between dimension.
 '    b. do not share a common edge to get the distance-between dimension.
 ' 3. Open an Immediate window.
 ' 4. Ensure that the latest SOLIDWORKS DimXpert type library is loaded:
 '    a. Select Tools > References.
 '    b. Click Browse.
 '    c. Find and select install_dir\swdimxpert.tlb.
 '
 ' Postconditions:
' 1. Inspect the Immediate window.
 ' 2. Observe the DistanceBetween1 or AngleBetween1 annotation on the
 '    DimXpertManager tab.
 '
 ' NOTE: Because this part is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
Option Explicit
 Dim dimXpertPart As dimXpertPart
Sub Main()
     Dim swapp As SldWorks.SldWorks
     Set swapp = Application.SldWorks
     Dim swModelDoc As SldWorks.ModelDoc2
     Set swModelDoc = swapp.ActiveDoc
     Dim annoType As Long

    If swModelDoc Is Nothing Then
      Exit Sub
    End If
     Dim dimXpertMgr As SldWorks.DimXpertManager
     Set dimXpertMgr = swapp.IActiveDoc2.Extension.DimXpertManager(swapp.IActiveDoc2.IGetActiveConfiguration().Name, True)
     Debug.Print "Model: " & swapp.IActiveDoc2.GetPathName
     Dim dimXpertPartObj As dimXpertPart
     Set dimXpertPartObj = dimXpertMgr.dimXpertPart
     Set dimXpertPart = dimXpertPartObj

     Dim dimOption As DimXpertDimensionOption
     Set dimOption = dimXpertPart.GetDimOption

     ' Specify a dimension along the normal to the face
     dimOption.DimensionPositionOption = 0

     ' Insert the dimension
     dimXpertPart.InsertLocationDimension dimOption

     Dim vAnnotations As Variant
     vAnnotations = dimXpertPart.GetAnnotations()
     Debug.Print "------------------------"
     Debug.Print "Annotations..."
     Debug.Print "------------------------"
     Dim annotationTemp As DimXpertAnnotation
     Dim annotationIndex As Long
     For annotationIndex = 0 To UBound(vAnnotations)
         Set annotationTemp = vAnnotations(annotationIndex)
         Call GeneralInfo(annotationTemp)
         annoType = annotationTemp.Type
         Call DimensionToleranceData(annotationTemp)
     Next
End Sub

Private Sub GeneralInfo(annotation As DimXpertAnnotation)
     Dim annoType As String
     Dim modelObj As Object
     Dim modelFeature As SldWorks.feature
     Debug.Print ""
     Debug.Print ("Name: " + annotation.Name)
     annoType = annotationTypeNameFromObject(annotation)
     Debug.Print ("Type: " + annoType)
     Debug.Print ("Display Entity: " + DisplayEntity(annotation))

     Set modelObj = annotation.GetModelFeature
     Set modelFeature = modelObj
     If Not (modelFeature Is Nothing) Then
         Debug.Print ("ModelFeature: " + modelFeature.Name + " (" + modelFeature.GetTypeName2() + ")")
     End If
End Sub
Private Sub DimensionToleranceData(annotation As DimXpertDimensionTolerance)
     Dim isAngleType As Boolean
     Dim annoType As Long
     Dim upper As Double, lower As Double
     Dim plus As Double, minus As Double
     Dim boolstatus As Boolean
     annoType = annotation.Type
     isAngleType = False
     Debug.Print ""
     Debug.Print ("Dimension Tolerance Compartment")

     If annoType = swDimXpertDimTol_DistanceBetween Then
         Dim distancebetween As DimXpertDistanceBetweenDimTol
         Set distancebetween = annotation
         Call DistanceBetweenData(distancebetween)
     ElseIf annoType = swDimXpertDimTol_AngleBetween Then
         isAngleType = True
         Dim angleBetween As IDimXpertAngleBetweenDimTol
         Set angleBetween = annotation
         ' the origin and tolerance feature
         Debug.Print ("Origin Feature: " + angleBetween.OriginFeature.Name)
         ' is supplement angle
         Debug.Print ("Supplement Angle: " + IIf(angleBetween.Supplement, "True", "False"))
    End If

     ' conversion for radians to degrees when dimension type is angle
     Dim dbl As Double
     If isAngleType Then
         dbl = 57.2957795130823
     Else
         dbl = 1#
     End If
     ' the nominal, and upper and lower limits of size of the dimension
     Debug.Print ("")
     Debug.Print ("Compute Nominal Dimension: " + FormatDouble(annotation.GetNominalValue * dbl))
     boolstatus = annotation.GetUpperAndLowerLimit(upper, lower)
     Debug.Print ("Get Upper Limit: " + FormatDouble(upper * dbl))
     Debug.Print ("Get Lower Limit: " + FormatDouble(lower * dbl))
     ' the upper and lower tolerance value by type
     Select Case annotation.DimensionType
     Case swDimXpertDimTolType_BlockTolerance
         Debug.Print ("Dimension Type: Block Tolerance")
     ' block tolerance
     Case swDimXpertDimTolType_BlockToleranceNoNominal
         Dim blockTols As DimXpertBlockTolerances
         Set blockTols = dimXpertPart.GetBlockTolerances
         Select Case blockTols.Type
             Case swDimXpertBlockToleranceType_ASMEInch
                 Debug.Print ("Dimension Type: Block Tolerance No Nominal")
                 If isAngleType Then
                     Debug.Print ("Angular Block Tolerance")
                 Else
                     Debug.Print ("Block Tolerance Decimal Places: " + Format(annotation.BlockToleranceDecimalPlaces, "##,##0"))
                 End If
             Case swDimXpertBlockToleranceType_ISO2768
                 Debug.Print ("Dimension Type: General Tolerance")
         End Select
     Case swDimXpertDimTolType_ISOLimitsAndFits
         Debug.Print ("Dimension Type: Limits and Fits")
     ' limits and fits tolerance
     Case swDimXpertDimTolType_ISOLimitsAndFitsNoNominal
         Debug.Print ("Dimension Type: Limits and Fits No Nominal")
         Debug.Print ("Limits and Fits: " + annotation.LimitsAndFitsCode)
     ' limit dimension
     Case swDimXpertDimTolType_LimitDimension
         Debug.Print ("Dimension Type: Limit Dimension")
         boolstatus = annotation.GetUpperAndLowerLimit(upper, lower)
         Debug.Print ("Get Upper Limit: " + FormatDouble(upper * dbl))
         Debug.Print ("Get Lower Limit: " + FormatDouble(lower * dbl))
     Case swDimXpertDimTolType_MAXTolerance
         Debug.Print ("Dimension Type: MAXTolerance")
     Case swDimXpertDimTolType_MINTolerance
         Debug.Print ("Dimension Type: MINTolerance")
     Case swDimXpertDimTolType_NoTolerance
         Debug.Print ("Dimension Type: NoTolerance")
     Case swDimXpertDimTolType_PlusMinusDimension
         Debug.Print ("Dimension Type: Plus Minus Dimension")
     ' plus and minus dimension
     Case swDimXpertDimTolType_PlusMinusNoNominal
         Debug.Print ("Dimension Type: Plus Minus No Nominal")
         boolstatus = annotation.GetPlusAndMinusTolerance(plus, minus)
         Debug.Print ("Plus  Tolerance: " + FormatDouble(plus * dbl))
         Debug.Print ("Minus Tolerance: " + FormatDouble(minus * dbl))
     End Select

 End Sub
Private Sub DistanceBetweenData(annotation As DimXpertDistanceBetweenDimTol)
     Dim feature As DimXpertFeature
     Dim featureFosUsage As Long
     Dim I As Double, J As Double, K As Double
     Dim boolstatus As Boolean
     ' the origin and tolerance feature along with their feature of size usage (min, max, center)
     boolstatus = annotation.GetOriginFeature(feature, featureFosUsage)
     Debug.Print ("")
     Debug.Print ("Origin Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage))
     boolstatus = annotation.GetFeature(feature, featureFosUsage)
     Debug.Print ("Tolerance Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage))
     ' The direction vector
     boolstatus = annotation.GetDirectionVector(I, J, K)
     Debug.Print ("")
     Debug.Print ("Direction Vector: " + FormatVector(I, J, K))
End Sub
Private Function annotationTypeNameFromObject(anno As DimXpertAnnotation) As String
     annotationTypeNameFromObject = annotationTypeNameFromTypeNumber(anno.Type)
 End Function
Private Function annotationTypeNameFromTypeNumber(annoTypeIndex As Long) As String
     Select Case annoTypeIndex
     Case swDimXpertDimTol_DistanceBetween
         annotationTypeNameFromTypeNumber = "DistanceBetween Dim"
     End Select
End Function
Private Function DisplayEntity(annotation As DimXpertAnnotation) As String
     Dim str As String
     Dim dispEnt As Object
     Dim swAnnot As SldWorks.annotation
     Set dispEnt = annotation.GetDisplayEntity
     If Not dispEnt Is Nothing Then
         If TypeOf dispEnt Is SldWorks.annotation Then
             Set swAnnot = dispEnt
             str = swAnnot.GetName
         End If
     End If
     DisplayEntity = str
End Function
Private Function FosUsage(value As Long) As String
     Dim str As String
     Select Case value
     Case swDimXpertDistanceFosUsage_Center
         str = "Center"
     Case swDimXpertDistanceFosUsage_MaximumSide
         str = "Max"
     Case swDimXpertDistanceFosUsage_MinimumSide
         str = "Min"
     Case Else
         str = "N/A"
     End Select
     FosUsage = str
End Function
Private Function FormatVector(I As Double, J As Double, K As Double) As String
     Dim str As String
     str = FormatDouble(I) + ", " + FormatDouble(J) + ", " + FormatDouble(K)
     FormatVector = str
End Function
Private Function FormatDouble(value As Double) As String
     Dim str
     str = Format(value, "##,##0.0000")
     FormatDouble = str
End Function
Private Function RadiansToDegrees(value As Double) As String
     Dim str
     str = Format((value * 57.2957795130823), "##,##0.00")
     RadiansToDegrees = str
End Function
```
