---
title: "Get More DimXpert Feature Examples (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Feature2_Example_VB.htm"
---

# Get More DimXpert Feature Examples (VBA)

This example shows how to build and get attributes for
the following DimXpert features:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Hole

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Notch

'---------------------------------------------------------------------------

' Preconditions:

'kadov_tag{{<spaces>}}1.
Open`public_documents`\samples\tutorial\api\cover_with_dimensions.sldprt.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2.
Open the DimXpert toolbar from**View > Toolbars**.

'kadov_tag{{<spaces>}}3.
Observe the following DimXpert features on the DimXpertManager tab:kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

' Simple
Hole and, Notch1.

'kadov_tag{{<spaces>}}4.
Open the Immediate window.

'kadov_tag{{<spaces>}}5.
Ensure that the latest SOLIDWORKS DimXpert type library is loaded

' in**Tools
> References**.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}6.
Step through this macro (F8).

'

' Postconditions: Compare
the output in the Immediate window

' with the features displayed on the DimXpertManager tab of the Management Panel.

'

'kadov_tag{{<spaces>}}NOTE:
Because this part is used elsewhere, do not save changes.

'--------------------------------------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As ModelDoc2

Dim swModelDocExt As ModelDocExtension

Dim swSelMgr As SelectionMgr

Dim swConfig As Configuration

Dim swFeature As feature

Dim swAnn As feature

Dim swSchema As DimXpertManager

Dim swDXPart As DimXpertPart

Dim featureType As swDimXpertFeatureType_e

Dim holeType AsswDimXpertCompoundHoleType_e

Dim features As Variant

Dim appliedFeatures As Variant

Dim appliedAnnotations As Variant

Dim appliedAnnotation As DimXpertAnnotation

Dim feature As DimXpertFeature

Dim appliedFeature As DimXpertFeature

Dim msgStr As String

Dim msgStr2 As String

Dim msgStr3 As String

Dim msgStr4 As String

Dim n As Long

Dim o As Long

Dim p As Long

Dim boolstatus As Boolean

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModelDocExt = swModel.Extension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the default DimXpert schema using IModelDocExtension.DimXpertManager()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSchema = swModelDocExt.DimXpertManager("Default", True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get IDimXpertPart from the IDimXpertManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDXPart = swSchema.DimXpertPart

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
featCount As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}featCount
= swDXPart.GetFeatureCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Total of "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= featCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= msgStr + msgStr2 + " features in " + (swSchema.SchemaName)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get IDimXpert features through IDimXpertPart

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}features
= swDXPart.GetFeatures

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= (swSchema.SchemaName) + " has the following features: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
n = 0 To UBound(features)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
feature = features(n)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Feature name: " + (feature.Name)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}featureType
= feature.Type

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Call
GetPatternType(featureType, msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Feature
type "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr3
= " is suppressed on the DimXpertManager tab? "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr4
= feature.IsSuppressed()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2 + msgStr3 + msgStr4

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Model feature: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeature = feature.GetModelFeature()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not (swFeature Is Nothing) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= swFeature.GetTypeName2()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Number of SOLIDWORKS face entities in this feature: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= feature.GetFaceCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Number of applied features: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= feature.GetAppliedFeatureCount()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}appliedFeatures
= feature.GetAppliedFeatures()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not (IsEmpty(appliedFeatures)) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
o = 0 To UBound(appliedFeatures)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
appliedFeature = appliedFeatures(o)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Applied feature name: " + (appliedFeature.Name)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Number of applied annotations: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= feature.GetAppliedAnnotationCount()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}appliedAnnotations
= feature.GetAppliedAnnotations()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not (IsEmpty(appliedAnnotations)) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
p = 0 To UBound(appliedAnnotations)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
appliedAnnotation = appliedAnnotations(p)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Applied annotation name: " + (appliedAnnotation.Name)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
If you know the name of a DimXpert feature, you can get it directly using
IDimXpertPart.GetFeature("name"),

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
which can return a general IDimXpertFeature or a more specific interface
on the feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
GetIDimXpertCompoundHoleFeaturefor the Simple Hole2 feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
holeFeature AsIDimXpertCompoundHoleFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
holeFeature = swDXPart.GetFeature("Simple Hole2")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= holeFeature.Name+ " is
a DimXpert feature"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the bottom feature if one exists

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bottomFeature As IDimXpertFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
bottomFeature = holeFeature.GetBottomFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not (bottomFeature Is Nothing) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Bottom feature is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= bottomFeature.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the reference feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
refFeature As IDimXpertFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
refFeature = holeFeature.GetReferenceFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Reference feature for dimensioning is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= refFeature.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the sub-feature count

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
count As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}count
= holeFeature.GetSubFeatureCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Number of subfeatures is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= count

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

' Get the sub-features

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
subfeatures As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}subfeatures
= holeFeature.GetSubFeatures

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
n = 0 To UBound(subfeatures)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
feature = subfeatures(n)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Sub-feature name: " + (feature.Name)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get whether the hole is blind

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Hole feature is blind and not through: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= holeFeature.Blind

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the type of the hole

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}holeType
= holeFeature.CompoundHoleType

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Hole feature is type: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Call
GetHoleType(holeType, msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
GetIDimXpertCompoundNotchFeaturefor the Notch1 feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
notchFeature AsIDimXpertCompoundNotchFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
notchFeature = swDXPart.GetFeature("Notch1")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= notchFeature.Name+ " is
a DimXpert feature"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the nominal notch coordinates

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
width As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
length As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
x As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
y As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
z As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
i As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
j As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
k As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
longitudeI As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
longitudeJ As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
longitudeK As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Nominal notch of Notch1"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= notchFeature.GetNominalNotch(width,
length, x, y, z, i, j, k, longitudeI, longitudeJ, longitudeK)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Width is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= width

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Length is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= length

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "X-coordinate is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= x

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Y-coordinate is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= y

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Z-coordinate is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= z

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "I-component of pierce vector is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "J-component of pierce vector is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= j

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "K-component of pierce vector is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= k

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "I-component of longitudinal unit vector is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= longitudeI

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "J-component of longitudinal unit vector is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= longitudeJ

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "K-component of longitudinal unit vector is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= longitudeK

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + msgStr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub

Public Sub GetPatternType(ByRef featureType, ByRef msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(featureType = swDimXpertFeature_Plane) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Plane"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeature_Cylinder) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Cylinder"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeature_Cone) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Cone"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeature_Extrude) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Extrude"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeature_Fillet) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Fillet"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeature_Chamfer) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Chamfer"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType =swDimXpertFeature_CompoundHole)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "CompoundHole"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeature_CompoundWidth) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "CompoundWidth"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType =swDimXpertFeature_CompoundNotch)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "CompoundNotch"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeature_CompoundClosedSlot3D) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "CompoundClosedSlot3D"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeature_IntersectPoint) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "IntersectPoint"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeature_IntersectLine) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "IntersectLine"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeature_IntersectCircle) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "IntersectCircle"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeature_IntersectPlane) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "IntersectPlane"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeature_Pattern) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Pattern"

ElseIf (featureType = swDimXpertFeature_Sphere) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Sphere"

ElseIf (featureType = swDimXpertFeature_BestfitPlane)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Bestfit plane"

ElseIf (featureType = swDimXpertFeature_Surface) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Surface"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub

Public Sub GetHoleType(ByRef holeType, ByRef msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(holeType = swDimXpertCompoundHoleType_Compound)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Compound"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(holeType =swDimXpertCompoundHoleType_Counterbore)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Counterbore"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(holeType =swDimXpertCompoundHoleType_Countersink)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Countersink"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(holeType =swDimXpertCompoundHoleType_Simple)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Simple"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub
