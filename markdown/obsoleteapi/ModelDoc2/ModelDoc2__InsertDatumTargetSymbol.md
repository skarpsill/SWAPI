---
title: "ModelDoc2::InsertDatumTargetSymbol"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertDatumTargetSymbol.htm"
---

# ModelDoc2::InsertDatumTargetSymbol

This method is obsolete and has been superseded
by[ModelDocExtension::InsertDatumTargetSymbol2](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__InsertDatumTargetSymbol2.htm).

Description

This method creates a datum target symbol.

Syntax (OLE Automation)

retval = ModelDoc2.InsertDatumTargetSymbol ( datum1,
datum2, datum3, areaStyle, areaOutside, value1, value2, valueStr1, valueStr2,
arrowsSmart, arrowStyle, leaderLineStyle, leaderBent, showArea, showSymbol
)

(Table)=========================================================

| Input: | (BSTR) datum1 | Datum reference string 1 |
| --- | --- | --- |
| Input: | (BSTR) datum2 | Datum reference string 2 |
| Input: | (BSTR) datum3 | Datum reference string 3 |
| Input: | (short) areaStyle | 0
= point 1
= circle 2
= rectangle |
| Input: | (VARIANT_BOOL) areaOutside | TRUE displays the target area dimensions size outside |
| Input: | (double) value1 | Numeric datum target area diameter or width |
| Input: | (double) value2 | Numeric datum target area height |
| Input: | (BSTR) valueStr1 | String value for datum target area diameter or width |
| Input: | (BSTR) valueStr2 | String value for datum target area height |
| Input: | (VARIANT_BOOL) arrowsSmart | TRUE uses smart arrows |
| Input: | (short) arrowStyle | Arrow head style as defined in swArrowStyle_e |
| Input: | (short) leaderLineStyle | Leaderline type as defined in swLeaderStyle_e |
| Input: | (VARIANT_BOOL) leaderBent | TRUE creates a bent leader line |
| Input: | (VARIANT_BOOL) showArea | TRUE shows the target area |
| Input: | (VARIANT_BOOL) showSymbol | TRUE displays the target symbol |
| Output: | (VARIANT_BOOL )retval | TRUE if created successfully; FALSE otherwise |

Syntax (COM)

status = ModelDoc2->InsertDatumTargetSymbol (
datum1, datum2, datum3, areaStyle, areaOutside, value1, value2, valueStr1,
valueStr2, arrowsSmart, arrowStyle, leaderLineStyle, leaderBent, showArea,
showSymbol, &retval )

(Table)=========================================================

| Input: | (BSTR) datum1 | Datum reference string 1 |
| --- | --- | --- |
| Input: | (BSTR) datum2 | Datum reference string 2 |
| Input: | (BSTR) datum3 | Datum reference string 3 |
| Input: | (short) areaStyle | 0
= point 1
= circle 2
= rectangle |
| Input: | (VARIANT_BOOL) areaOutside | TRUE displays the target area dimensions size outside |
| Input: | (double) value1 | Numeric datum target area diameter or width |
| Input: | (double) value2 | Numeric datum target area height |
| Input: | (BSTR) valueStr1 | String value for datum target area diameter or width |
| Input: | (BSTR) valueStr2 | String value for datum target area height |
| Input: | (VARIANT_BOOL) arrowsSmart | TRUE uses smart arrows |
| Input: | (short) arrowStyle | Arrow head style as defined in swArrowStyle_e |
| Input: | (short) leaderLineStyle | Leaderline type as defined in swLeaderStyle_e |
| Input: | (VARIANT_BOOL) leaderBent | TRUE creates a bent leader line |
| Input: | (VARIANT_BOOL) showArea | TRUE shows the target area |
| Input: | (VARIANT_BOOL) showSymbol | TRUE displays the target symbol |
| Output: | (VARIANT_BOOL) retval | TRUE if created successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Parameters Table Start

Remarks

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__InsertDatumTargetSymbol.htm" >
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
<param name="Items" value="ModelDoc2 Method$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__InsertDatumTargetSymbol.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
