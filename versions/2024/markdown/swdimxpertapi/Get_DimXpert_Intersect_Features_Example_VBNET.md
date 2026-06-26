---
title: "Get DimXpert Intersect Features Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Intersect_Features_Example_VBNET.htm"
---

# Get DimXpert Intersect Features Example (VB.NET)

This example shows how to build a part and get attributes
for the following DimXpert features:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Intersect
Point

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Intersect
Line

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Intersect
Circle

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Intersect
Plane

'---------------------------------------------------------------------------

' Preconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1.
Open`public_documents`\samples\tutorial\api\face_plate_ads_geo.sldprt.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}2.
Open the DimXpert toolbar from**View > Toolbars**.

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}3.
Create an Intersect Point DimXpert Feature:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}a.
Click**Location Dimension**on the DimXpert toolbar.

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}b.
Select the front face of the part.

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}c. Select**Create Intersection Point**on the DimXpert
shorcut menu.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}d.
Select a cylinder whose axis intersects the first face at a point.

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}e.
Click the green check mark in the shortcut menu to create the

' intersect
point.

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}f.
Select a feature on the part to dimension against the intersect point.

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}g.
Click to position the dimension in the view.

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}h.
Observe the new DimXpert feature on the DimXpertManager tab:kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

'**Intersect
Point1**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}4.
Create an Intersect Line DimXpert Feature:

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}a.
Click**Location Dimension**on the DimXpert toolbar.

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}b.
Select the front face of the part.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}c. Select**Create Intersection Line**from the DimXpert
shortcut menu.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}d.
Select a perpendicular plane that would intersect the first plane

' if extended
(e.g., a top or side face of the part).

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}e.
Click the green check mark in the shortcut menu to create the

' intersect
line.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}f.
Select a feature on the part to dimension against the intersect line.

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}g.
Click to position the dimension in the view.

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}h.
Observe the new DimXpert feature on the DimXpertManager tab:kadov_tag{{<spaces>}}

'kadov_tag{{</spaces>}}**Intersect
Line1**

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}5.
Create an Intersect Circle DimXpert Feature:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}a.
Click**Size Dimension**on the DimXpert toolbar.

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}b.
Select the front face of the part.

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}c. Select**Intersect Circle**from the DimXpert
shortcut menu.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}d.
Select the opening conical surface of a flat head machine screw

' (**LPattern1**or**LPattern3**) in the part.

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}e.
Click the green check mark in the shortcut menu to finish the dimension.

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}f.
Click to position the size dimension in the view.

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}g.
Observe the new DimXpert feature on the DimXpertManager tab:kadov_tag{{<spaces>}}

'kadov_tag{{</spaces>}}**Intersect
Circle1**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}6.
Create an Intersect Plane DimXpert Feature:

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}a. Click**Location Dimension**on the DimXpert toolbar.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}b.
Zoom in on a flat head machine screw (**LPattern1**or**LPattern3**).

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}c.
Select the opening conical surface of a flat head machine screw

' in the
part.

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}d.
Select**Intersect Plane**from the DimXpert shortcut menu.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}e.
Select the inner cylindrical bore face of the flat head machine screw.

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}f.
Click the green check mark in the shortcut menu to create the

' intersect
plane.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}g.
Select the top face of one of the extruded entities.

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}h.
Click to position the location dimension in the view.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}i.
Observe the new DimXpert feature on the DimXpertManager tab:kadov_tag{{<spaces>}}

'kadov_tag{{</spaces>}}**Intersect
Plane1**

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}7.
Open an Immediate window.

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}8.
Ensure that the latestSolidWorks.Interop.swdimxpert.dllinterop

' assembly is loaded (right-click
project in Project Explorer and

' click**Add Reference**> .**NET**tab).

kadov_tag{{<spaces>}}'

kadov_tag{{<spaces>}}'
Postconditions: Compare
the output in the Immediate Window

' with the features displayed on the DimXpertManager tab of the Management Panel.

'

kadov_tag{{<spaces>}}'kadov_tag{{<spaces>}}NOTE:
Because this part is used elsewhere, do not save changes.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'----------------------------------------------------------------------------

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
feature1 As IDimXpertFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
feature2 As IDimXpertFeature

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
radius As Double

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
Get IDimXpertIntersectCircleFeature
for the Intersect Circle1 feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
iCircleFeature As IDimXpertIntersectCircleFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iCircleFeature
= swDXPart.**GetFeature**("Intersect Circle1")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= iCircleFeature.Name+ "
is a DimXpert intersect circle feature"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the nominal circle parameters

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= iCircleFeature.GetNominalCircle(radius,
x, y, z, i, j, k)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
boolstatus Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}The
nominal circle has the following parameters:"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Radius
is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= radius

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}x-coordinate
is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= x

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}y-coordinate
is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= y

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}z-coordinate
is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= z

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}i-component
of pierce vector is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}j-component
of pierce vector is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= j

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}k-component
of pierce vector is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= k

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get IDimXpertIntersectLineFeature
for the Intersect Line1 feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
iLineFeature As IDimXpertIntersectLineFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iLineFeature
= swDXPart.**GetFeature**("Intersect Line1")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= iLineFeature.Name+ " is
a DimXpert intersect line feature"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the nominal line parameters

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= iLineFeature.GetNominalLine(x,
y, z, i, j, k)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
boolstatus Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}The
nominal line has the following parameters:"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}x-coordinate
is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= x

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}y-coordinate
is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= y

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}z-coordinate
is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= z

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}i-component
of pierce vector is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}j-component
of pierce vector is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= j

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}k-component
of pierce vector is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= k

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get IDimXpertIntersectPlaneFeature
for the Intersect Plane1 feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
iPlaneFeature As IDimXpertIntersectPlaneFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iPlaneFeature
= swDXPart.GetFeature("Intersect Plane1")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= iPlaneFeature.Name+ "
is a DimXpert intersect plane feature"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the two features used to construct the intersect plane

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= iPlaneFeature.GetFeatures(feature1,
feature2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}The
plane intersects the following DimXpert features:"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Feature1
is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= feature1.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Feature2
is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= feature2.**Name**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get IDimXpertIntersectPointFeature
for the Intersect Point1 feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
iPointFeature As IDimXpertIntersectPointFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iPointFeature
= swDXPart.**GetFeature**("Intersect Point1")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= iPointFeature.Name+ "
is a DimXpert intersect point feature"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the nominal point

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= iPointFeature.GetNominalPoint(x,
y, z)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
boolstatus Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}The
nominal point has the following parameters:"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}x-coordinate
is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= x

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}y-coordinate
is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= y

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}z-coordinate
is "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= z

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(msgStr
+ msgStr2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
Sub GetPatternType(ByRef featureType As swDimXpertFeatureType_e,
ByRef msgStr2 As String)

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
