---
title: "Gtol::SetFrameSymbols"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Gtol/Gtol__SetFrameSymbols.htm"
---

# Gtol::SetFrameSymbols

This method is obsolete and has been superseded
by[Gtol::SetFrameSymbols2](sldworksAPI.chm::/Gtol/Gtol__SetFrameSymbols2.htm).

Description

This
method sets all the symbols for a feature control symbol.

Syntax (OLE Automation)

void
Gtol.SetFrameSymbols ( frameNumber, GCS, tolDia1, tolMC1, tolDia2, tolMC2,
datumMC1, datumMC2, datumMC3)

(Table)=========================================================

| Input: | (short)
frameNumber | Feature
control frame 1 for first |
| --- | --- | --- |
| Input: | (short)
GCS | Geometric
characteristic symbol |
| Input: | (BOOL)
tolDia1 | Diameter
symbol exists for tolerance 1 (TRUE or FALSE) |
| Input: | (short)
tolMC1 | Material
condition for tolerance 1 |
| Input: | (BOOL)
tolDia2 | Diameter
symbol exists for tolerance 2 (TRUE or FALSE) |
| Input: | (short)
tolMC2 | Material
condition for tolerance 2 |
| Input: | (short)
datumMC1 | Material
condition for primary datum |
| Input: | (short)
datumMC2 | Material
condition for secondary datum |
| Input: | (short)
datumMC3 | Material
condition for tertiary datum |

Syntax (COM)

status
= Gtol->SetFrameSymbols ( frameNumber, GCS, tolDia1, tolMC1, tolDia2,
tolMC2, datumMC1, datumMC2, datumMC3 )

(Table)=========================================================

| Input: | (short)
frameNumber | Feature
control frame 1 for first |
| --- | --- | --- |
| Input: | (short)
GCS | Geometric
characteristic symbol |
| Input: | (VARIANT_BOOL)
tolDia1 | Diameter
symbol exists for tolerance 1 (TRUE or FALSE) |
| Input: | (short)
tolMC1 | Material
condition for tolerance 1 |
| Input: | (VARIANT_BOOL)
tolDia2 | Diameter
symbol exists for tolerance 2 (TRUE or FALSE) |
| Input: | (short)
tolMC2 | Material
condition for tolerance 2 |
| Input: | (short)
datumMC1 | Material
condition for primary datum |
| Input: | (short)
datumMC2 | Material
condition for secondary datum |
| Input: | (short)
datumMC3 | Material
condition for tertiary datum |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

For valid Geometric Characteristic Symbols
(GCS), refer to swGtolGeomCharSymbol_e.

For valid Material Conditions (tolMC1,
tolMC2, datumMC1, and so on), refer to swGtolMatCondition_e.

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
<param name="Items" value="Gtol_Object$$**$$ZGetSetFrameSymbols$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\sw2003\Gtol\Gtol__SetFrameSymbols.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
