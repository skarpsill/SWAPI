---
title: "ModelDoc::GridOptions"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GridOptions.htm"
---

# ModelDoc::GridOptions

This
method is obsolete and has been superseded by[ModelDoc2::GridOptions](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GridOptions.htm).

Description

This method sets the options for the grid.

Syntax (OLE Automation)

void ModelDoc.GridOptions
( dispGrid, gridSpacing, snap, dotStyle, nMajor, nMinor, align2edge, angleSnap,
angleUnit, minorAuto)

(Table)=========================================================

| Input: | (BOOL) dispGrid | TRUE to display the grid, FALSE otherwise |
| --- | --- | --- |
| Input: | (double) gridSpacing | Snap distance |
| Input: | (BOOL) snap | TRUE to snap to grid, FALSE otherwise |
| Input: | (BOOL) dotStyle | TRUE for dotted grids, FALSE otherwise |
| Input: | (short) nMajor | Number of minors in major |
| Input: | (short) nMinor | Number of snaps in minor |
| Input: | (BOOL) align2edge | TRUE if to be aligned to an edge, FALSE otherwise |
| Input: | (BOOL) angleSnap | TRUE to snap to angle, FALSE otherwise |
| Input: | (double) angleUnit | Value of angle to which to snap |
| Input: | (BOOL) minorAuto | TRUE if the minor grids are to be set automatically, FALSE otherwise |

Syntax
(COM)

status = ModelDoc->GridOptions
( dispGrid, gridSpacing, snap, dotStyle, nMajor, nMinor, align2edge, angleSnap,
angleUnit, minorAuto )

(Table)=========================================================

| Input: | (VARIANT_BOOL) dispGrid | TRUE to display the grid, FALSE otherwise |
| --- | --- | --- |
| Input: | (double) gridSpacing | Snap distance |
| Input: | (VARIANT_BOOL) snap | TRUE to snap to grid, FALSE otherwise |
| Input: | (VARIANT_BOOL) dotStyle | TRUE for dotted grids, FALSE otherwise |
| Input: | (short) nMajor | Number of minors in major |
| Input: | (short) nMinor | Number of snaps in minor |
| Input: | (VARIANT_BOOL) align2edge | TRUE if to be aligned to an edge, FALSE otherwise |
| Input: | (VARIANT_BOOL) angleSnap | TRUE to snap to angle, FALSE otherwise |
| Input: | (double) angleUnit | Value of angle to which to snap |
| Input: | (VARIANT_BOOL) minorAuto | TRUE if the minor grids are to be set automatically, FALSE otherwise |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The align2edge parameter aligns the grid with the currently selected
edge. If align2edge is set to TRUE, then you must have an edge selected.

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
<param name="Items" value="ModelDoc_Object$$**$$ZSketchOptions$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc\ModelDoc__GridOptions.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
