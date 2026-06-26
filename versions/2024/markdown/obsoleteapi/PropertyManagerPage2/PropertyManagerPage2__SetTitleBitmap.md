---
title: "PropertyManagerPage2::SetTitleBitmap"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2/PropertyManagerPage2__SetTitleBitmap.htm"
---

# PropertyManagerPage2::SetTitleBitmap

This method is obsolete and has been superseded
by[PropertyManagerPage2::SetTitleBitmap2](sldworksAPI.chm::/PropertyManagerPage2/PropertyManagerPage2__SetTitleBitmap2.htm).

Description

This method sets the bitmap in the title bar
of this PropertyManager.

Syntax (OLE Automation)

retval = PropertyManagerPage2.SetTitleBitmap ( ModuleHandle,
Identifier )

(Table)=========================================================

| Input: | (long) ModuleHandle | Module handle of the application instance that contains the bitmap resource |
| --- | --- | --- |
| Input: | (long) Identifier | Resource ID of the bitmap |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |

Syntax (COM)

status = PropertyManagerPage2->SetTitleBitmap
( ModuleHandle, Identifier, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (long) ModuleHandle | Module handle of the application instance that contains the bitmap resource |
| --- | --- | --- |
| Input: | (long) Identifier | Resource ID of the bitmap |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can only use this method to set properties
on the PropertyManager page before it is displayed or while it is closed.
See PropertyManagerPage2::Show and PropertyManagerPage2::Close for details.

Create the bitmap in the resources of your application.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}The bitmap
must have less than 256 colors. It is accessed via the ModuleHandle and
Identifier that is passed into this API.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}The
recommended size for bitmaps is a square from 18- to 22-cells wide.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}However,
the bitmap can be any size, as long as it fits on the title bar.

The bitmap appears transparent by mapping any white
(RGB(255,255,255)) cells to the current Property Manager page title bar
background color.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Remember
the special use of this color as you design your bitmap.

(Table)=========================================================

| If this method is... | Then the title bar contains... |
| --- | --- |
| Used | Specified bitmap starting at the left edge of the PropertyManager title
bar, followed by the title bar text (see SldWorks::CreatePropertyManagerPage). |
| Not used | Only the text, centered on the title bar. |

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\PropertyManagerPage2\PropertyManagerPage2__SetTitleBitmap.htm" >
<param name="_ID" value="RelatedTopic2" >
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
<param name="Items" value="PropertyManagerPage2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\PropertyManagerPage2\PropertyManagerPage2__SetTitleBitmap.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
