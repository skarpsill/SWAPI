---
title: "ChamferFeatureData::Type"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ChamferFeatureData/ChamferFeatureData__Type.htm"
---

# ChamferFeatureData::Type

This
property is obsolete and has been superseded by[ChamferFeatureData2::Type](sldworksAPI.chm::/ChamferFeatureData2/ChamferFeatureData2__Type.htm).

Description

This property gets or sets the chamfer feature
type.

Syntax (OLE Automation)

chamferType= ChamferFeatureData.Type (VB
Get property)

ChamferFeatureData.Type =chamferType(VB
Set property)

chamferType= ChamferFeatureData.GetType ( ) (C++ Get
property)

ChamferFeatureData.SetType (chamferType) (C++ Set property)

(Table)=========================================================

| Property: | ( int ) chamferType | Type of the Chamfer feature (see below) |
| --- | --- | --- |

Syntax (COM)

status = ChamferFeatureData ->get_Type ( &chamferType)

status = ChamferFeatureData ->put_Type (chamferType)

(Table)=========================================================

| Property: | ( int ) chamferType | Type of the Chamfer feature (see below) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The chamfer feature type should have one of the values below.

- 1 = Angle-Distance
- 2 = Distance-Distance
- 3 = Vertex

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
<param name="Items" value="ZFeatureDefinition$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ChamferFeatureData\ChamferFeatureData__Type.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
