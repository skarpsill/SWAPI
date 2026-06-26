---
title: "Face::Highlight"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__Highlight.htm"
---

# Face::Highlight

This
method is obsolete and has been superseded by[Face2::Highlight](sldworksAPI.chm::/Face2/Face2__Highlight.htm).

Description

This method highlights or de-highlights this face object.

Syntax (OLE Automation)

void
Face.Highlight ( state)

(Table)=========================================================

| Input: | (BOOL)
state | TRUE
highlights the face, FALSE de-highlights the face |
| --- | --- | --- |

Syntax (COM)

status
= Face->IHighlight ( state )

(Table)=========================================================

| Input: | (VARIANT_BOOL)
state | TRUE
highlights the face, FALSE de-highlights the face |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

The highlight state remains
in place until the model is rebuilt or redrawn.

SolidWorks does not support this method for faces obtained from reference
surface bodies.

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Face_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Face\Face__Highlight.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan
