---
title: "Gtol::GetFrameSymbols"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Gtol/Gtol__GetFrameSymbols.htm"
---

# Gtol::GetFrameSymbols

This method is obsolete and has been superseded by[Gtol::GetFrameSymbols2](sldworksAPI.chm::/Gtol/Gtol__GetFrameSymbols2.htm)and[Gtol::GetFrameDiameterSymbols](sldworksAPI.chm::/Gtol/Gtol__GetFrameDiameterSymbols.htm).

Description

This method returns an array describing the symbols that appear in the
first or second feature control frame of this Gtol.

Syntax (OLE Automation)

retval
= Gtol.GetFrameSymbols ( frameNumber)

(Table)=========================================================

| Input: | (short)
frameNumber | Frame
number |
| --- | --- | --- |
| Return: | (VARIANT)
retval | VARIANT
of type SafeArray |

Syntax (COM)

status
= Gtol->IGetFrameSymbols ( frameNumber, retval )

(Table)=========================================================

| Input: | (short)
frameNumber | Frame
number |
| --- | --- | --- |
| Output: | (short*)
retval | Array
of shorts |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

Each symbol returned by this method is identified by an integer index
that you can use as the symIdx argument with the GetSym* methods.

Format of return information is the following array of short integers:

retval[0] = gcs, Geometric characteristic
symbol index

retval[1] = tdia1, Indicates whether the
first gtol tolerance has a "diameter" symbol

retval[2] = tmc1, Index of material condition
symbol for first tolerance value

retval[3] = tdia2, Indicates whether the
second gtol tolerance has a "diameter" symbol

retval[4] = tmc2, Index of material condition
symbol for first tolerance value

retval[5] = dmc1, Index of material condition
symbol for datum1

retval[6] = dmc2, Index of material condition
symbol for datum2

retval[7] = dmc3, Index of material condition
symbol for datum3

For valid Geometric Characteristic Symbols
(GCS), see swGtolGeomCharSymbol_e.

For valid Material Conditions (tolMC1,
tolMC2, datumMC1, and so on), see swGtolMatCondition_e.

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
<param name="Items" value="Gtol_Object$$**$$ZGetSetFrameSymbols$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Gtol\Gtol__GetFrameSymbols.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
