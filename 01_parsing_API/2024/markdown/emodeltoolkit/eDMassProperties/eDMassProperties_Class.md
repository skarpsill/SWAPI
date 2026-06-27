---
title: "eDMassProperties Class"
project: ""
interface: "eDMassProperties"
member: ""
kind: "class"
source: "emodeltoolkit/eDMassProperties/eDMassProperties_Class.htm"
---

# eDMassProperties Class

(Generated Script Links)========================================

(Generated Code)================================================

(WARNING: DO NOT EDIT OR DELETE THIS SECTION!)==================

begin!kadov{{===================================================

}}end!kadov=====================================================

(==============================================================)

(Table)=========================================================

| See
Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Contains mass, volume, surface area, and center of gravity data. Use
metric units (kg, m^3, m^3, m).

#### Header file code

classkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}eDMassProperties

{

public:

eDMassProperties(
double mass, double volume, double area, const double cg[ 3 ] )

: _mass( mass ), _volume( volume ), _area(
area )

{

_cg[ 0 ] = _cg[ 1 ] = _cg[ 2 ] = 0;

if ( cg )

{

_cg[ 0 ] = cg[ 0 ];

_cg[ 1 ] = cg[ 1 ];

_cg[ 2 ] = cg[ 2 ];

}

}

double GetMass() const { return _mass; }

double GetVolume() const { return _volume;
}

double GetArea() const { return _area; }

void GetCG( double cg[ 3 ] ) const { cg[
0 ] = _cg[ 0 ]; cg[ 1 ] = _cg[ 1 ]; cg[ 2 ] = _cg[ 2 ]; }

bool IsValid() const

{

return _mass > 0 || _volume > 0 ||
_area > 0;

};

};

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
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
<param name="Items" value="DocumentGeometryClasses$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\eModelToolkit\eDMassProperties\eDMassProperties_Class.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan

begin!kadov{{

}}end!kadov

kadov_tag{{<implicit_p>}}

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
<param name="Items" value="ZGeteDMassProperties$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\eModelToolkit\eDMassProperties\eDMassProperties_Class.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan
