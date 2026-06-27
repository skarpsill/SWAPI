---
title: "ModelDoc::SetAddToDB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetAddToDB.htm"
---

# ModelDoc::SetAddToDB

This method is obsolete
and has been superseded by[ModelDoc2::SetAddToDB](../ModelDoc2/ModelDoc2__SetAddToDB.htm).

Description

This method sets whether sketch entities are added directly to the SolidWorks
database.

Syntax (OLE Automation)

void ModelDoc.SetAddToDB ( setting)

(Table)=========================================================

| Input: | (BOOL) setting | TRUE if you want items added directly to the SolidWorks database, FALSE
otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->SetAddToDB (
setting )

(Table)=========================================================

| Input: | (VARIANT_BOOL) setting | TRUE if you want items added directly to the SolidWorks database, FALSE
otherwise |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

One of the benefits of adding sketch entities directly to the database
is that you can avoid grid and entity snapping. For example, if you create
a sketch line whose endpoint is near another entity or near a grid point,
the new line endpoint will snap to the other item or grid point. Using
SetAddToDB( True ) will avoid this behavior during sketch entity creation.

The[SetAddToDB](ModelDoc__SetAddToDB.htm)and[SetDisplayWhenAdded](ModelDoc__SetDisplayWhenAdded.htm)functions will also will increase performance during sketch entity creation.[SetDisplayWhenAdded](ModelDoc__SetDisplayWhenAdded.htm)requires
that SetAddToDB is TRUE.

If you want to constrain all the sketch entities after creation, you
can use the Sketch::ConstrainAll function.

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
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__SetAddToDB.htm" >
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
<param name="Items" value="Direct_Add_to_Database_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__SetAddToDB.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
