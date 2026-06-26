---
title: "Surface::ICreateTrimmedSheet2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Surface/Surface__ICreateTrimmedSheet2.htm"
---

# Surface::ICreateTrimmedSheet2

This method is obsolete and has been superseded
by[Surface::ICreateTrimmedSheet3](Surface__ICreateTrimmedSheet3.htm).

Description

This method creates a trimmed
sheet body from this surface.

Syntax (OLE Automation)

See Surface::CreateTrimmedSheet.

Syntax (COM)

status = Surface->ICreateTrimmedSheet2 ( nCurves,
curves, &sheet )

Parameters Table Start

(Table)=========================================================

| Input: | (long) nCurves | Number of curves in the array of curves |
| --- | --- | --- |
| Input: | (LPCURVE*) curves | Array of curve pointers that represent the boundary
of the sheet |
| Output: | (LPBODY2) sheet | Pointer to the newly created sheet body |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The array of curves represents all of the curves
required to add the appropriate trimming loops to the surface. A NULL
entry in the array represents the separation between loops.

The curves supplied are assumed to lie on the surface.
If the curves are 2D curves, then they should be created using this surface.

If the application is creating a trimmed sheet body from an input periodical
surface without trimming curves, then the curve array may be empty.

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
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Surface\Surface__ICreateTrimmedSheet2.htm" >
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
<param name="Items" value="Surface_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Surface\Surface__ICreateTrimmedSheet2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
