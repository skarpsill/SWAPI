---
title: "Face::IGetTrimCurveSize2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__IGetTrimCurveSize2.htm"
---

# Face::IGetTrimCurveSize2

This
method is obsolete and has been superseded by[Face2::IGetTrimCurveSize2](sldworksAPI.chm::/Face2/Face2__IGetTrimCurveSize2.htm).

Description

Thismethodreturns the size of the array needed to hold data for[Face::IGetTrimCurve](Face__GetTrimCurves2.htm).

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Face->IGetTrimCurveSize2
( wantCubic, wantNRational, &retval )

(Table)=========================================================

| Input: | (VARIANT_BOOL) wantCubic | TRUE if the trim curves are to be cubic, FALSE if not |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) wantNRational | TRUE if the trim curves are to be non-rational, FALSE if not |
| Output: | (long) retval | Size of the array required for Face::IGetTrimCurve |
| Return: | (HRESULT)status | S_OK if successful |

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Face_Object$$**$$ZGetInfoFace$$**$$ZGetInfoSurface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sjesse\sw2001Plus\Face\Face__IGetTrimCurveSize2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
