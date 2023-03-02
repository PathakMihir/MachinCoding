package core

var store map[string]*ValueObj

func Init() {
	store = make(map[string]*ValueObj)

}

type ValueObj struct {
	Value     interface{}
	ExpiresAt int64
}

func NewValueObj(value interface{}, duration int64) *ValueObj {

	var expiresAt int64 = -1

	if duration > 0 {
		//expiresAt=time.Now().UnixMilli() +duration
	}

	return &ValueObj{
		Value:     value,
		ExpiresAt: expiresAt,
	}
}

func Put(k string, value *ValueObj) {
	store[k] = value
}

func Get(k string) *ValueObj {
	return store[k]
}
