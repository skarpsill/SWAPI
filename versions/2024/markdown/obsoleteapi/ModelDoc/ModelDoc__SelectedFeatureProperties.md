---
title: "ModelDoc::SelectedFeatureProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SelectedFeatureProperties.htm"
---

# ModelDoc::SelectedFeatureProperties

This method is obsolete
and has been superseded by[ModelDoc2::SelectedFeatureProperties](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SelectedFeatureProperties.htm).

Description

This method sets the property values of the selected feature.

Syntax (OLE Automation)

retval = ModelDoc.SelectedFeatureProperties
( rgbColor, ambient, diffuse, specular, shininess, transparency, emission,
usePartProps, suppressed, featureName)

(Table)=========================================================

| Input: | (long) rgbColor | Feature color |
| --- | --- | --- |
| Input: | (double) ambient | Feature ambient value; valid range is from 0 to 1 |
| Input: | (double) diffuse | Feature diffuse value; valid range is from 0 to 1 |
| Input: | (double) specular | Feature specular value; valid range is from 0 to 1 |
| Input: | (double) shininess | Feature shininess value; valid range is from 0 to 1 |
| Input: | (double) transparency | Feature transparency value; valid range is from 0 to 1 |
| Input: | (double) emission | Feature emission value; valid range is from 0 to 1 |
| Input: | (BOOL) usePartProps | TRUE if the feature will inherit the part properties, FALSE otherwise |
| Input: | (BOOL) suppressed | TRUE if the feature is suppressed, FALSE otherwise |
| Input: | (BSTR) featureName | Name of the feature |
| Return: | (BOOL) retval | TRUE if successfully changed the feature properties, FALSE otherwise |

Syntax (COM)

status =
ModelDoc->SelectedFeatureProperties ( rgbColor, ambient, diffuse, specular,
shininess, transparency, emission, usePartProps, suppressed, featureName,
&retval )

(Table)=========================================================

| Input: | (long) rgbColor | Feature color |
| --- | --- | --- |
| Input: | (double) ambient | Feature ambient value; valid range is from 0 to 1 |
| Input: | (double) diffuse | Feature diffuse value; valid range is from 0 to 1 |
| Input: | (double) specular | Feature specular value; valid range is from 0 to 1 |
| Input: | (double) shininess | Feature shininess value; valid range is from 0 to 1 |
| Input: | (double) transparency | Feature transparency value; valid range is from 0 to 1 |
| Input: | (double) emission | Feature emission value; valid range is from 0 to 1 |
| Input: | (VARIANT_BOOL) usePartProps | TRUE if the feature will inherit the Part properties, FALSE otherwise |
| Input: | (VARIANT_BOOL) suppressed | TRUE if the feature is suppressed, FALSE otherwise |
| Input: | (BSTR) featureName | Name of the feature |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully changed the feature properties, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is different from ModelDoc::SelectedFaceProperties and ModelDoc::SelectedEdgeProperties
in that it will allow you to change the name of this feature. The reasoning
is that all features have names;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}whereas,
a face or edge typically have a name only if it is being referenced. Because
it is dangerous to change the name of a referenced object, we do not allow
you to programmatically change the names of faces or edges. See Feature::Name
and PartDoc::SetEntityName.

This method requires the feature to be selected. To select the feature
programmatically, you can use ModelDoc::SelectByID and pass in the feature
name along with the appropriate object type (for example,"BODYFEATURE",
"ATTRIBUTE", "PLANE", "SKETCH", and so on)
and the selection coordinates 0,0,0. You can determine the feature name
and object type using Feature::Name and Feature::GetTypeName,kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}respectively.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZModifyNames$$**$$ZModifyFeature$$**$$ZSetNames$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SelectedFeatureProperties.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
