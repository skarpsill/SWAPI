---
title: "ModelDoc::SetDisplayWhenAdded"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetDisplayWhenAdded.htm"
---

# ModelDoc::SetDisplayWhenAdded

This method is obsolete
and has been superseded by[ModelDoc2::SetDisplayWhenAdded](../ModelDoc2/ModelDoc2__SetDisplayWhenAdded.htm).

Description

This method sets whether new sketch entities are displayed upon creation.
The sketch entities will appear on the screen once a ModelDoc::GraphicsRedraw2
or ModelDoc::EditRebuild is performed (ModelDoc::GraphicsRedraw2 is much
faster than an ModelDoc::EditRebuild).

Syntax (OLE Automation)

void ModelDoc.SetDisplayWhenAdded (
setting)

(Table)=========================================================

| Input: | (BOOL) setting | TRUE if new sketch entities are to be displayed when added, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->SetDisplayWhenAdded
( setting )

(Table)=========================================================

| Input: | (VARIANT_BOOL) setting | TRUE if new sketch entities are to be displayed when added, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This setting remains even after your program run has ended. Therefore,
it is recommended that you reset this parameter to TRUE at the end of
your program. For example, if you have ended your program and the display
is set to FALSE, then the user would have difficulty performing selections
and newly created entities would not be seen until a redraw or a rebuild.

The ModelDoc::SetAddToDB and ModelDoc::SetDisplayWhenAdded functions
also increase performance during sketch entity creation.

NOTE:ModelDoc::SetDisplayWhenAdded
settings are ignored unless ModelDoc::SetAddToDB is TRUE.

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
<param name="Items" value="ModelDoc_Object$$**$$ZGetSetAddToDB$$**$$ZGetSetDisplayWhenAdded$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__SetDisplayWhenAdded.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
