---
title: "Surface::IGetBSurfParamsSize"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Surface/Surface__IGetBSurfParamsSize.htm"
---

# Surface::IGetBSurfParamsSize

This method is obsolete and has been superseded
by[Surface::IGetBSurfParamsSize2](Surface__IGetBSurfParamsSize2.htm).

Description

This method gets the allocation size necessary for Bsurface parameter
data retrieval in a subsequent call to Surface::GetBSurfParams.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Surface->IGetBSurfParamsSize
( wantCubicRational, Range, &retval )

(Table)=========================================================

| Input: | (VARIANT_BOOL) wantCubicRational | TRUE if you want surface to be a cubic rational, FALSE otherwise |
| --- | --- | --- |
| Input: | (double*) Range | Pointer to an array of 4 doubles describing the U,V Range; these four
values are upper and lower U and V bounds, respectively; these values
can be obtained using Surface::Parameterization |
| Output: | (long) retval | Size of the data set |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Range contains the following values which can be obtained using Surface::Parameterization:

- Range[0] & Range[2] are
  the lower bounds of the U & V surface parameters, respectively.
- Range[1] & Range[3] are
  the upper bounds of the U & V surface parameters, respectively.

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
<param name="Items" value="Surface_Object$$**$$ZGetInfoSurface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\Surface\Surface__IGetBSurfParamsSize.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
