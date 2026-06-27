---
title: "Get More DimXpert Feature Examples (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Feature2_Example_VBNET.htm"
---

# Get More DimXpert Feature Examples (VB.NET)

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
Hole2 and Notch1.

'kadov_tag{{<spaces>}}4.
Open the Immediate window.

'kadov_tag{{<spaces>}}5.
Ensure that the latestSolidWorks.Interop.swdimxpert.dllinterop assembly

' is loaded (right-click
the project in Project Explorer and

' click**Add Reference >**.NET
tab)

'kadov_tag{{<spaces>}}6.
Step through this macro (F8).

'

' Postconditions: Compare
the output in the Immediate Window

' with the features displayed on the DimXpertManager tab of the Management Panel.

'

'kadov_tag{{<spaces>}}NOTE:
Because this part is used elsewhere, do not save changes.

'---------------------------------------------------------------------------

Imports SolidWorks.Interop.sldworks

Imports SolidWorks.Interop.swdimxpert

Imports SolidWorks.Interop.swconst

Imports System

Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModel As IModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelDocExt As IModelDocExtension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgr As ISelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swConfig As IConfiguration

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFeature As IFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAnn As IFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSchema As IDimXpertManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDXPart As IDimXpertPart

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
featureType As swDimXpertFeatureType_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
holeType AsswDimXpertCompoundHoleType_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
features As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
appliedFeatures As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
appliedAnnotations As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
appliedAnnotation As IDimXpertAnnotation

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
feature As IDimXpertFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
appliedFeature As IDimXpertFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
msgStr As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
msgStr2 As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
msgStr3 As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
msgStr4 As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
n As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
o As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
p As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
boolstatus As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel
= swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModelDocExt
= swModel.Extension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelMgr
= swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the default DimXpert schema using IModelDocExtension.DimXpertManager()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSchema
= swModelDocExt.DimXpertManager("Default", True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get IDimXpertPart from the IDimXpertManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDXPart
= swSchema.DimXpertPart

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

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get IDimXpert features through IDimXpertPart

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}features
= swDXPart.GetFeatures

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= (swSchema.SchemaName) + " has the following features: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
n = 0 To UBound(features)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}feature
= features(n)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Feature name: " + (feature.Name))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}featureType
= feature.Type

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Call
GetPatternType(featureType, msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Feature
type "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr3
= " is suppressed on the DimXpertManager tab? "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr4
= feature.IsSuppressed()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2 + msgStr3 + msgStr4)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Model feature: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFeature
= feature.GetModelFeature()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not (swFeature Is Nothing) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= swFeature.GetTypeName2()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Number of SOLIDWORKS face entities in this feature: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= feature.GetFaceCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Number of applied features: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= feature.GetAppliedFeatureCount()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}appliedFeatures
= feature.GetAppliedFeatures()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not (IsNothing(appliedFeatures)) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
o = 0 To UBound(appliedFeatures)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}appliedFeature
= appliedFeatures(o)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Applied feature name: " + (appliedFeature.Name))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Number of applied annotations: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= feature.GetAppliedAnnotationCount()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}appliedAnnotations
= feature.GetAppliedAnnotations()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not (IsNothing(appliedAnnotations)) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
p = 0 To UBound(appliedAnnotations)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}appliedAnnotation
= appliedAnnotations(p)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Applied annotation name: " + (appliedAnnotation.Name))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
If you know the name of a DimXpert feature, you can get it directly using
IDimXpertPart.GetFeature("name"),

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
which can return a general IDimXpertFeature or a more specific interface
on the feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get IDimXpertCompoundHoleFeature for the Simple Hole2 feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
holeFeature AsIDimXpertCompoundHoleFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}holeFeature
= swDXPart.GetFeature("Simple Hole2")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= holeFeature.Name+ " is
a DimXpert feature"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the bottom feature if one exists

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bottomFeature As IDimXpertFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bottomFeature
= holeFeature.GetBottomFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not (bottomFeature Is Nothing) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Bottom feature is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= bottomFeature.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the reference feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
refFeature As IDimXpertFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}refFeature
= holeFeature.GetReferenceFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Reference feature for dimensioning is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= refFeature.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

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

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get whether the hole is blind

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Hole feature is blind and not through: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= holeFeature.Blind

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the type of the hole

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}holeType
= holeFeature.CompoundHoleType

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Hole feature is type: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Call
GetHoleType(holeType, msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get IDimXpertCompoundNotchFeature for the Notch1 feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
notchFeature AsIDimXpertCompoundNotchFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}notchFeature
= swDXPart.GetFeature("Notch1")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= notchFeature.Name+ " is
a DimXpert feature"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the nominal notch coordinates

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

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Nominal
notch of Notch1")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= notchFeature.GetNominalNotch(width,
length, x, y, z, i, j, k, longitudeI, longitudeJ, longitudeK)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Width is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= width

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Length is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= length

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "X-coordinate is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= x

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Y-coordinate is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= y

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Z-coordinate is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= z

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "I-component of unit vector is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "J-component of unit vector is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= j

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "K-component of unit vector is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= k

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Longitudinal i-component of pierce unit vector is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= longitudeI

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Longitudinal j-component of pierce unit vector is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= longitudeJ

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Longitudinal k-component of pierce unit vector is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= longitudeK

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
Sub GetPatternType(ByRef featureType As swDimXpertFeatureType_e, ByRef
msgStr2 As String)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_Plane) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Plane"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_Cylinder) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Cylinder"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_Cone) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Cone"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_Extrude) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Boss"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_Fillet) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Fillet"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_Chamfer) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Chamfer"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_CompoundHole)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "CompoundHole"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_CompoundWidth)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "CompoundWidth"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_CompoundNotch)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "CompoundNotch"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_CompoundClosedSlot3D)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "CompoundClosedSlot3D"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_IntersectPoint)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "IntersectPoint"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_IntersectLine)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "IntersectLine"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_IntersectCircle)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "IntersectCircle"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_IntersectPlane)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "IntersectPlane"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_Pattern) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Pattern"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_Sphere) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Sphere"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_BestfitPlane)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Bestfit plane"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_Surface) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Surface"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
Sub GetHoleType(ByRef holeType AsswDimXpertCompoundHoleType_e,
ByRef msgStr2 As String)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(holeType = swDimXpertCompoundHoleType_e.swDimXpertCompoundHoleType_Compound)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Compound"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(holeType = swDimXpertCompoundHoleType_e.swDimXpertCompoundHoleType_Counterbore)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Counterbore"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(holeType = swDimXpertCompoundHoleType_e.swDimXpertCompoundHoleType_Countersink)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Countersink"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(holeType = swDimXpertCompoundHoleType_e.swDimXpertCompoundHoleType_Simple)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Simple"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
swApp As SldWorks

End Class
