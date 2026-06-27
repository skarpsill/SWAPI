---
title: "ModelDoc::GetFeatureCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetFeatureCount.htm"
---

# ModelDoc::GetFeatureCount

This
method is obsolete and has been superseded by[ModelDoc2::GetFeatureCount.](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetFeatureCount.htm)

Description

This method returns the number of features in this document.

Syntax (OLE Automation)

retval = ModelDoc.GetFeatureCount ()

(Table)=========================================================

| Return: | (long) retval | Number of features in this document, excluding nay subfeatures |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetFeatureCount
( &retval )

(Table)=========================================================

| Output: | (long) retval | Number of features in this document, excluding nay subfeatures |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The number of features returned by this method
does not include subfeatures. Subfeatures include, for example, mate features
within a mate group, drawing views on a sheet,kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}and
so on. One way to identify a subfeature is whether it can be returned
by Feature::GetFirstSubFeature or Feature::GetNextSubFeature.

This method returns the number of features returned
when traversing the feature list with ModelDoc::FirstFeature and Feature::GetNextFeature.
This value may be useful in feature traversal or in accessing the feature
by position using ModelDoc::FeatureByPositionReverse.

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
<param name="Items" value="ModelDoc_Object$$**$$ZGetInfoFeature$$**$$ModelDoc::FeatureByPositionReverse$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__GetFeatureCount.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
