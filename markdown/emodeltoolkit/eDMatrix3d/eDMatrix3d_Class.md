---
title: "eDMatrix3d Class"
project: ""
interface: "eDMatrix3d"
member: ""
kind: "class"
source: "emodeltoolkit/eDMatrix3d/eDMatrix3d_Class.htm"
---

# eDMatrix3d Class

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

Represents a 3D rotation matrix.

#### Header file code

class eDMatrix3d

{

public:

eDMatrix3d();

eDMatrix3d( double
xx, double xy, double xz, double yx, double yy, double yz, double zx,
double zy, double zz );

eDMatrix3d( const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&xv, const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&yv, const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&zv );

eDMatrix3d( const eDMatrix3d
&p );

eDMatrix3d( const double
p[9] );

double get_xx() const;

double get_xy() const;

double get_xz() const;

double get_yx() const;

double get_yy() const;

double get_yz() const;

double get_zx() const;

double get_zy() const;

double get_zz() const;

double operator[](
int i ) const;

double & operator[](
int i );

eDPt3d x_vec() const;

eDPt3d y_vec() const;

eDPt3d z_vec() const;

double determinant()
const;

eDMatrix3d inverse();

eDMatrix3d normalize()
const;

eDMatrix3d transpose()
const;

eDMatrix3d mult( const
eDMatrix3d &p ) const;

[eDPt3d](../eDPt3d/eDPt3d_Class.htm)mult( const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&v ) const;

eDMatrix3d mult( double
d ) const;

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
<param name="Items" value="" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\eModelToolkit\eDMatrix3d\eDMatrix3d_Class.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="-1" >
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
<param name="Items" value="ZGeteDMatrix3d$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\eModelToolkit\eDMatrix3d\eDMatrix3d_Class.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan
