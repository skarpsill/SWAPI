---
title: "ModelDoc::Parameter"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__Parameter.htm"
---

# ModelDoc::Parameter

This
method is obsolete and has been superseded by[ModelDoc2::Parameter](sldworksAPI.chm::/ModelDoc2/ModelDoc2__Parameter.htm).

Description

This method returns a pointer to the parameter
or to the Dispatch object. Most parameters are dimensions.

Syntax (OLE Automation)

retval = ModelDoc.Parameter ( stringIn)

(Table)=========================================================

| Input: | (BSTR) stringIn | Name of parameter (feature@name@component@assembly) |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to Dispatch object, the parameter |

Syntax (COM)

status = ModelDoc->IParameter (
stringIn, &retval )

(Table)=========================================================

| Input: | (BSTR) stringIn | Name of parameter (feature@name@component@assembly). |
| --- | --- | --- |
| Output: | (LPDIMENSION) retval | Pointer to the parameter |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The stringIn argument must be the fully qualified
dimension name; for example,Error! Reference
source not found."D1@Base-Extrude. You do not need to use
the full dimension if you are calling, for example, the Feature::Parameter
function.

SolidWorks recognizes some characters as special
characters. The use of these characters in names of parts or features
can cause the this method to fail to return a dimension. Special characters
are: at sign (@),
the period (.), and the slash (/).

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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZGetParameter$$**$$ZGetDimension$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__Parameter.htm" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Change_Dimension_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__Parameter.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
