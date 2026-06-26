---
title: "Get DimXpert Extrude Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Extrude_Feature_Example_VBNET.htm"
---

# Get DimXpert Extrude Feature Example (VB.NET)

This example shows how to build a part and get attributes for the DimXpert
Extrude feature.

'-----------------------------------------------------------------------------

' Preconditions:

'kadov_tag{{<spaces>}}1.
Open`public_documents`\samples\tutorial\api\plate_ads_plusminus.sldprt.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2.
Open the DimXpert toolbar from**View > Toolbars**.

'kadov_tag{{<spaces>}}3.
Create the Extrude Feature:

'kadov_tag{{<spaces>}}a. Click**Auto Dimension Scheme**on the DimXpert toolbar.

'kadov_tag{{<spaces>}}b.
Ensure the**Scope**is set to**All Features**.

'kadov_tag{{<spaces>}}c.
Click the green check mark to accept the settings.

'kadov_tag{{<spaces>}}4.
Observe the following DimXpert features on the DimXpertManager tab:kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

' Hole
Pattern1 and Pocket1.

'kadov_tag{{<spaces>}}5.
Open the Immediate window.

'kadov_tag{{<spaces>}}6.
Ensure that theSolidWorks.Interop.swdimxpert.dllinterop assembly

' is loaded (right-click
project in Project Explorer and

' click**Add Reference**>**.NET**tab).

'

' Postconditions: Compare
the output in the Immediate Window

' with the features displayed on the DimXpertManager tab of the Management Panel.

'

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}NOTE:
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
= swApp.**ActiveDoc**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModelDocExt
= swModel.**Extension**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelMgr
= swModel.**SelectionManager**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the default DimXpert schema using IModelDocExtension.DimXpertManager()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSchema
= swModelDocExt.**DimXpertManager**("Default", True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get IDimXpertPart from the IDimXpertManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDXPart
= swSchema.**DimXpertPart**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
featCount As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}featCount
= swDXPart.**GetFeatureCount**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Total of "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= featCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= msgStr + msgStr2 + " DimXpert features in " + (swSchema.**SchemaName**)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get IDimXpert features through IDimXpertPart

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}features
= swDXPart.**GetFeatures**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= (swSchema.**SchemaName**) + " has the following features: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
n = 0 To UBound(features)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}feature
= features(n)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Feature name: " + (feature.**Name**))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}featureType
= feature.**Type**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Call
GetPatternType(featureType, msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Feature
type "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr3
= " is suppressed on the DimXpertManager tab? "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr4
= feature.**IsSuppressed**()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2 + msgStr3 + msgStr4)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Model feature: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFeature
= feature.**GetModelFeature**()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not (swFeature Is Nothing) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= swFeature.**GetTypeName2**()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Number of SOLIDWORKS face entities in this feature: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= feature.**GetFaceCount**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Number of applied features: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= feature.**GetAppliedFeatureCount**()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}appliedFeatures
= feature.**GetAppliedFeatures**()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not (IsNothing(appliedFeatures)) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
o = 0 To UBound(appliedFeatures)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}appliedFeature
= appliedFeatures(o)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Applied feature name: " + (appliedFeature.**Name**))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Number of applied annotations: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= feature.**GetAppliedAnnotationCount**()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}appliedAnnotations
= feature.**GetAppliedAnnotations**()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not (IsNothing(appliedAnnotations)) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
p = 0 To UBound(appliedAnnotations)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}appliedAnnotation
= appliedAnnotations(p)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Applied annotation name: " + (appliedAnnotation.**Name**))

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
Get IDimXpertExtrudeFeature for the Pocket1 feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
extrudeFeature As IDimXpertExtrudeFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}extrudeFeature
= swDXPart.**GetFeature**("Pocket1")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= extrudeFeature.Name+ "
is a DimXpert extrude feature"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the bottom blends

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}feature
= extrudeFeature.GetBottomBlends

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not feature Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "The bottom blends for the extrude is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= feature.**Name**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Else
: Debug.Print("There are no bottom blends for this extrude.")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the bottom feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}feature
= extrudeFeature.GetBottomFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not feature Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "The bottom feature for the extrude is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= feature.**Name**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the reference feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}feature
= extrudeFeature.GetReferenceFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not feature Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "The reference feature for the extrude is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= feature.**Name**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the sub-features

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
featureCount As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}featureCount
= extrudeFeature.GetSubFeatureCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "The number of sub-features of the extrude is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= featureCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}features
= extrudeFeature.GetSubFeatures

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
n = 0 To UBound(features)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}feature
= features(n)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ "Feature name: " + (feature.**Name**))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}featureType
= feature.**Type**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Call
GetPatternType(featureType, msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Feature
type is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get whether the extrude is blind

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= extrudeFeature.Blind

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "The extrude is blind: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= boolstatus

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

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
= "Extrude"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_Fillet)
Then

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
= "Bestfit Plane"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(featureType = swDimXpertFeatureType_e.swDimXpertFeature_Surface) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= "Surface"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
swApp As SldWorks

End Class
