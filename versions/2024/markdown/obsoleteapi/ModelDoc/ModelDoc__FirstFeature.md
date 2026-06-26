---
title: "ModelDoc::FirstFeature"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FirstFeature.htm"
---

# ModelDoc::FirstFeature

This
method is obsolete and has been superseded by[ModelDoc2::FirstFeature](sldworksAPI.chm::/ModelDoc2/ModelDoc2__FirstFeature.htm).

Description

This returns the first feature in the document.

Syntax (OLE Automation)

retval = ModelDoc.FirstFeature ()

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Pointer to Dispatch object for the first feature in the document |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IFirstFeature
( &retval )

(Table)=========================================================

| Output: | (LPFEATURE) retval | Pointer to the first feature in the document |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For access to the next feature in the FeatureManager design tree and
access to subfeatures, seekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Feature::GetNextFeature
and Feature::GetFirstSubFeature, respectively.

If a feature is suppressed, this method still accesses the feature.

Your application should not assume that the name or the order of SolidWorks
features is always the same. For example, you should not assume that the
first feature in the list is always be a reference plane. Additionally,
because feature names are customizable, you cannot assume that the first
reference plane feature is named Plane1. See Feature::GetTypeName and
Feature::Name for details.

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
<param name="Items" value="ModelDoc_Object$$**$$ZGetFeature$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__FirstFeature.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
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
<param name="Items" value="Feature_Suppression_Example$$**$$Get_Feature_and_SubFeature_Example$$**$$Get_Sketches_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__FirstFeature.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
