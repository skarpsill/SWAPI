---
title: "eDPt3d Class"
project: ""
interface: "eDPt3d"
member: ""
kind: "class"
source: "emodeltoolkit/eDPt3d/eDPt3d_Class.htm"
---

# eDPt3d Class

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

Represents a point or vector in 3D space.

#### Header file code

class eDPt3d

{

public:

eDPt3d( double xc =
0, double yc = 0, double zc = 0 );

eDPt3d( const double
c[ 3 ] );

eDPt3d( const eDPt3d
& );

eDPt3d &operator=(
const eDPt3d & );

double x() const;

double y() const;

double z() const;

void set_x( double
t );

void set_y( double
t );

void set_z( double
t );

double operator[](
int i ) const;

double &operator[](
int i );

double norm() const;

eDPt3d normalize()
const;

eDPt3d operator-();

eDPt3d &operator-=(
const eDPt3d &p );

eDPt3d &operator+=(
const eDPt3d &p );

eDPt3d &operator*=(
double d );

eDPt3d &operator/=(
double d );

bool coincident( const
eDPt3d &p, double tol = POS_EPSILON ) const;

friend eDPt3d operator-(
const eDPt3d &, const eDPt3d & );

friend eDPt3d operator+(
const eDPt3d &, const eDPt3d & );

friend double operator%(
const eDPt3d &, const eDPt3d & );

friend eDPt3d operator*(
double, const eDPt3d & );

friend eDPt3d operator*(
const eDPt3d &, double );

friend eDPt3d operator*(
const eDPt3d &, const eDPt3d & );

friend eDPt3d operator/(
const eDPt3d &, double );

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
<param name="Items" value="MathClasses$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\eModelToolkit\eDPt3d\eDPt3d_Class.htm" >
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
<param name="Items" value="ZGeteDPt3d$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\eModelToolkit\eDPt3d\eDPt3d_Class.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan
