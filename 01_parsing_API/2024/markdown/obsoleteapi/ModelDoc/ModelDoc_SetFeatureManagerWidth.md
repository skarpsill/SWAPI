---
title: "ModelDoc::SetFeatureManagerWidth"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc_SetFeatureManagerWidth.htm"
---

# ModelDoc::SetFeatureManagerWidth

This method is obsolete and has been superseded
by[ModelDoc2::SetFeatureManagerWidth](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetFeatureManagerWidth.htm).

Description

This method sets the width of the Feature Manager
design tree in pixels.

Syntax (OLE Automation)

retval = ModelDoc.SetFeatureManagerWidth (width)

(Table)=========================================================

| Input: | (long) width | Width of the FeatureManager design tree view,
in pixels |
| --- | --- | --- |
| Output: | (long) retval | Status of the set width operation |

Syntax (COM)

status = ModelDoc->SetFeatureManagerWidth ( width,
&retval )

(Table)=========================================================

| Input: | (long) width | Width of the FeatureManager design tree view,
in pixels |
| --- | --- | --- |
| Output: | (long) retval | Status of the set width operation |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The retval argument indicates the success or failure
of the set width operation. A value of 0 indicates the window width was
successfully set. A value of -1 indicates that the window width was not
successfully set.

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
<param name="Items" value="ModelDoc_Object$$**$$ZModifyUserInterface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc_SetFeatureManagerWidth.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
