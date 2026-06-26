---
title: "ModelDoc::IsOpenedViewOnly"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__IsOpenedViewOnly.htm"
---

# ModelDoc::IsOpenedViewOnly

This
method is obsolete and has been superseded by[ModelDoc2::IsOpenedViewOnly](sldworksAPI.chm::/ModelDoc2/ModelDoc2__IsOpenedViewOnly.htm).

Description

This method determines if a SolidWorks document is open in view-only
mode.

Syntax (OLE Automation)

retval = ModelDoc.IsOpenedViewOnly
( )

(Table)=========================================================

| Return: | (Boolean)retval | TRUE if this document is view-only, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IsOpenedViewOnly
( &retval )

(Table)=========================================================

| Output: | (VARIANT_BOOL)retval | TRUE if this document is view-only, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

SolidWorks loads files using multi-threading. When a file is being loaded,
the graphics are displayed immediately and the user is able to perform
certain zoom and pan functions. If the view is shaded, you also have the
option to rotate the view. Until all data and references have been loaded,
the file is in view-only mode. Also, a file can be in view-only mode if
the user has chosen to load the file for viewing purposes. A user can
do this by selectingFile, Openand toggling the view-only button to on. Your application should check
for view-only mode to determine how to proceed.

When a file is in view-only mode, many API queries will return NULL
or empty data.

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
<param name="Items" value="ModelDoc_Object$$**$$ZGetInfoModelDoc$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__IsOpenedViewOnly.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
