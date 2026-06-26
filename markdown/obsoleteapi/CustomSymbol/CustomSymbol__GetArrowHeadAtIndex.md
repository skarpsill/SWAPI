---
title: "CustomSymbol::GetArrowHeadAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetArrowHeadAtIndex.htm"
---

# CustomSymbol::GetArrowHeadAtIndex

This method is obsolete and has been superseded
by[Note::GetArrowHeadAtIndex](sldworksAPI.chm::/Note/Note__GetArrowHeadAtIndex.htm).

Description

This
method gets information on the specified arrow head in this custom symbol.

Syntax (OLE Automation)

retval
= CustomSymbol.GetArrowHeadAtIndex ( index)

(Table)=========================================================

| Input: | (long)
index | Index
of the desired arrow head where the index begins at zero |
| --- | --- | --- |
| Return: | (VARIANT)
retval | VARIANT
of type SafeArray of doubles |

Syntax (COM)

status = CustomSymbol->IGetArrowHeadAtIndex
( index, retval )

(Table)=========================================================

| Input: | (long) index | Index of the desired arrow head where the index begins at zero |
| --- | --- | --- |
| Output: | (double*) retval | Pointer to an array of doubles |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is an array of doubles in the
following format:

[arrowHeadPt[3],arrowHeadDir[3],arrowHeadWidth,arrowHeadHeight,arrowHeadStyle]

(Table)=========================================================

| arrowHeadPt [3] | XYZ arrow head tip location |
| --- | --- |
| arrowHeadDir [3] | XYZ arrow head direction |
| arrowHeadWidth | Arrow head width where the width is measured along the arrow head direction |
| arrowHeadHeight | Arrow head height |
| arrowHeadStyle | Arrow head style as defined in swArrowStyle_e |

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
<param name="Items" value="CustomSymbol_Object$$**$$ZGetInfoCustomSymbol$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\CustomSymbol\CustomSymbol__GetArrowHeadAtIndex.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
