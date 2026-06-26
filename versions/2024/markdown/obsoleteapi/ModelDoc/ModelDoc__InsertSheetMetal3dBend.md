---
title: "ModelDoc::InsertSheetMetal3dBend"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertSheetMetal3dBend.htm"
---

# ModelDoc::InsertSheetMetal3dBend

T his
method is obsolete and has been superseded by[ModelDoc2::InsertSheetMetal3dBend](../ModelDoc2/ModelDoc2__InsertSheetMetal3dBend.htm).

Description

This method inserts a sheet metal 3D bend.

Syntax (OLE Automation)

void ModelDoc.InsertSheetMetal3dBend ( angle, radius,
flipDir, bendPos)

(Table)=========================================================

| Input: | (double) angle | Angle of the bend that you are inserting |
| --- | --- | --- |
| Input: | (double) radius | Radius of the bend you are inserting |
| Input: | (BOOL) flipDir | TRUE to flip the bend direction, FALSE otherwise |
| Input: | (short) bendPos | Value of the bend position |

Syntax (COM)

status = ModelDoc->InsertSheetMetal3dBend ( angle,
radius, flipDir, bendPos )

(Table)=========================================================

| Input: | (double) angle | Angle of the bend that you are inserting. |
| --- | --- | --- |
| Input: | (double) radius | Radius of the bend you are inserting |
| Input: | (VARIANT_BOOL) flipDir | TRUE to flip the bend direction, FALSE otherwise |
| Input: | (short) bendPos | Value of the bend position |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The value of the bend positions are:

- 0 =
  Bend centerline
- 1 =
  Material inside
- 2 =
  Material outside
- 3 =
  Bend 0utside

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
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc\ModelDoc__InsertSheetMetal3dBend.htm" >
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
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc\ModelDoc__InsertSheetMetal3dBend.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
