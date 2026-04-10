package main

import (
	"reflect"
	"testing"
)

func TestRobot(t *testing.T) {
	// Инициализация робота: ширина 6, высота 3
	obj := Constructor(6, 3)

	// Описываем шаги теста
	steps := []struct {
		name    string
		action  string // "step", "getPos", "getDir"
		val     int    // для step
		wantPos []int
		wantDir string
	}{
		{"Move 2", "step", 2, nil, ""},
		{"Move 2 more", "step", 2, nil, ""},
		{"Check Pos", "getPos", 0, []int{4, 0}, ""},
		{"Check Dir", "getDir", 0, nil, "East"},
		{"Move 2 to corner", "step", 2, nil, ""},
		{"Move 2 to corner", "step", 1, nil, ""},
		{"Move 2 to corner", "step", 4, nil, ""},
		{"Check Pos at corner", "getPos", 0, []int{1, 2}, ""}, // Пример, зависит от логики поворота
		{"Check Dir at corner", "getDir", 0, nil, "West"},
	}

	for _, tt := range steps {
		t.Run(tt.name, func(t *testing.T) {
			switch tt.action {
			case "step":
				obj.Step(tt.val)
			case "getPos":
				if got := obj.GetPos(); !reflect.DeepEqual(got, tt.wantPos) {
					t.Errorf("GetPos() = %v, want %v", got, tt.wantPos)
				}
			case "getDir":
				if got := obj.GetDir(); got != tt.wantDir {
					t.Errorf("GetDir() = %v, want %v", got, tt.wantDir)
				}
			}
		})
	}
}


/*

6*2 = 12; 3*2 = 6; 18

*/
func TestRobot1(t *testing.T) {
	// Инициализация робота: ширина 6, высота 3
	obj := Constructor(6, 3)

	// Описываем шаги теста
	steps := []struct {
		name    string
		action  string // "step", "getPos", "getDir"
		val     int    // для step
		wantPos []int
		wantDir string
	}{
		{"Move 20", "step", 20, nil, ""},
		{"Check Pos", "getPos", 0, []int{5, 1}, ""},
		{"Check Dir", "getDir", 0, nil, "North"},
	}

	for _, tt := range steps {
		t.Run(tt.name, func(t *testing.T) {
			switch tt.action {
			case "step":
				obj.Step(tt.val)
			case "getPos":
				if got := obj.GetPos(); !reflect.DeepEqual(got, tt.wantPos) {
					t.Errorf("GetPos() = %v, want %v", got, tt.wantPos)
				}
			case "getDir":
				if got := obj.GetDir(); got != tt.wantDir {
					t.Errorf("GetDir() = %v, want %v", got, tt.wantDir)
				}
			}
		})
	}
}

/*

6*2 = 12; 3*2 = 6; 18

*/
func TestRobot2(t *testing.T) {
	// Инициализация робота: ширина 6, высота 3
	obj := Constructor(6, 3)

	// Описываем шаги теста
	steps := []struct {
		name    string
		action  string // "step", "getPos", "getDir"
		val     int    // для step
		wantPos []int
		wantDir string
	}{
		{"Move 14", "step", 14, nil, ""},
		{"Check Pos", "getPos", 0, []int{0,0}, ""},
		{"Check Dir", "getDir", 0, nil, "South"},
		{"Move 5", "step", 5, nil, ""},
		{"Check Pos", "getPos", 0, []int{5,0}, ""},
		{"Check Dir", "getDir", 0, nil, "East"},
	}

	for _, tt := range steps {
		t.Run(tt.name, func(t *testing.T) {
			switch tt.action {
			case "step":
				obj.Step(tt.val)
			case "getPos":
				if got := obj.GetPos(); !reflect.DeepEqual(got, tt.wantPos) {
					t.Errorf("GetPos() = %v, want %v", got, tt.wantPos)
				}
			case "getDir":
				if got := obj.GetDir(); got != tt.wantDir {
					t.Errorf("GetDir() = %v, want %v", got, tt.wantDir)
				}
			}
		})
	}
}
