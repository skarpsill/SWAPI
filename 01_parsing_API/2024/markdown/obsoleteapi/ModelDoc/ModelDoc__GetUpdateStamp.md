---
title: "ModelDoc::GetUpdateStamp"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetUpdateStamp.htm"
---

# ModelDoc::GetUpdateStamp

This
method is obsolete and has been superseded by[ModelDoc2::GetUpdateStamp](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetUpdateStamp.htm).

Description

This method returns the current update stamp for
this document.

Syntax (OLE Automation)

retval = ModelDoc.GetUpdateStamp ()

(Table)=========================================================

| Return: | (long) retval | Current update stamp value for this document |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetUpdateStamp
( &retval )

(Table)=========================================================

| Output: | (long) retval | Current update stamp value for this document |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The update stamp is essentially an integer form
of a time stamp. The update stamp is incremented for model state changes
(for example,kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}suppressing
or unsuppressing features in a model, configuration changes, feature changes,
and so on) and for geometric changes (for example, anything that requires
a rebuild). This time stamp is not incremented for operations such as
color changes, feature or configuration name changes, and so on.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__GetUpdateStamp.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
