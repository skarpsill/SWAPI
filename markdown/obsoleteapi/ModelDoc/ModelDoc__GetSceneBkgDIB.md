---
title: "ModelDoc::GetSceneBkgDIB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetSceneBkgDIB.htm"
---

# ModelDoc::GetSceneBkgDIB

This
method is obsolete and has been superseded by[ModelDoc2::GetSceneBkgDIB](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetSceneBkgDIB.htm).

Description

This method gets background image as a LPDIBSECTION.

Syntax (OLE Automation)

l_dib = ModelDoc.GetSceneBkgDIB
( )

(Table)=========================================================

| Return: | (long) l_dib | Background image as DIBSECTION |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetSceneBkgDIB
( &l_dib )

(Table)=========================================================

| Output: | (long)l_dib | Background image as DIBSECTION |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For more information, see Bitmap structures, DIBSECTION
in MicroSoft Help.

The memory for the image bits ( DIBSECTION.dsBm.bmBits)
and this structure are allocated by SolidWorks and must be deleted by
the caller.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZGetInfoModelView$$**$$ZGetSetSceneBkgDIB$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__GetSceneBkgDIB.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
